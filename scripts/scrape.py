import urllib
import json
import time
import sys
from bs4 import BeautifulSoup


# We'd so like not to have to scrape this and just use the API but we can't ...
# http://developer.github.com/changes/2013-10-18-new-code-search-requirements/
def get_list_from_github():
    url = 'https://github.com/search?l=json&q=name+resources+filename%3Adatapackage.json+path%3A%2F&type=Code'
    failuresLeft = 5

    fo = urllib.urlopen(url)
    if (fo.getcode() >= 400):
      print('Status code: %s' % fo.getcode())
      return []

    soup = BeautifulSoup(fo.read())
    # total number of results
    total = int(soup.select('.selected .counter')[0].get_text().replace(',', ''))
    print('According to github there are %s potential data packages' % total)

    # do the first one to save loading again
    try:
        out = extractReposFromPage(soup)
    except ValueError:
        print('First page of results did not contain any data packages')
        sys.exit(0)

    # now go through results pages - 10 results per page
    pagecount = int(total/10.0)+1
    for ii in range(2,pagecount+1):
        turl = url + '&p=%s' % ii
        print('Processing: %s' % turl)

        # Retry until the request succeeds
        while True:
            fo = urllib.urlopen(turl)
            if (fo.getcode() < 400):
                break

            print('ERROR! Status code: %s, sleeping for 1' % fo.getcode())
            time.sleep(1)

        body = fo.read()
        soup = BeautifulSoup(body)
        try:
            tmp = extractReposFromPage(soup)
        except ValueError:
            failuresLeft -= 1
            if failuresLeft <= 0:
                print('Got 5 pages that contained no data packages, exiting.')
                return out

            continue
        out += tmp
        # sleep to prevent github getting unhappy and 420'ing us
        if ii == 9:
            print('sleeping for 60')
            time.sleep(60)
        else:
            time.sleep(1)
    out.sort()
    return out

def extractReposFromPage(soup):
    out = []
    for et in soup.select('#code_search_results .title'):
        links = et.select('a')
        if len(links) < 2:
            print('Too few links for node %s' % et.get_text())
            continue

        userPlusRepo = links[0].get_text()
        filename = links[1].get_text()

        if filename != 'datapackage.json':
            print('Got file named "{0}" for "{1}" (expected datapackage.json)'.format(
                filename, userPlusRepo))
            continue

        url = 'https://github.com/' + userPlusRepo;
        out.append(url)

    if not out:
        raise ValueError('No data packages found in page')

    return out

if __name__ == '__main__':
    out = get_list_from_github()

    # Sort and deduplicate.
    out = sorted(set(out))
    print('Found %s data packages' % len(out))
    out = '\n'.join(out)
    open('catalog-list.txt', 'w').write(out)
