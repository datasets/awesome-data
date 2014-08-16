import urllib
import json
import time
from bs4 import BeautifulSoup


# We'd so like not to have to scrape this and just use the API but we can't ...
# http://developer.github.com/changes/2013-10-18-new-code-search-requirements/
def get_list_from_github():
    url = 'https://github.com/search?q=name+extension%3Ajson+path%3Adatapackage.json&type=Code&ref=searchresults'
    fo = urllib.urlopen(url)
    if (fo.getcode() >= 400):
      print('Status code: %s' % fo.getcode())
      return []

    soup = BeautifulSoup(fo.read())
    # total number of results
    total = int(soup.select('.selected .counter')[0].get_text())
    print('According to github there are %s data packages' % total)

    # do the first one to save loading again
    out = extractReposFromPage(soup)

    # now go through results pages - 10 results per page
    pagecount = int(total/10.0)+1
    for ii in range(2,pagecount+1):
        turl = url + '&p=%s' % ii
        print('Processing: %s' % turl)
        fo = urllib.urlopen(turl)
        if (fo.getcode() >= 400):
          print('ERROR! Status code: %s' % fo.getcode())
          continue
        body = fo.read()
        soup = BeautifulSoup(body)
        tmp = extractReposFromPage(soup)
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
    for el in soup.select('#code_search_results .title a:first-child'):
        userPlusRepo = el.get_text().strip()
        # some cases get results where data is just # datapackage.json (??)
        if userPlusRepo != 'datapackage.json':
            url = 'https://github.com/' + userPlusRepo
            out.append(url)
    return out

if __name__ == '__main__':
    out = get_list_from_github()
    print('Found %s data packages' % len(out))
    out = '\n'.join(out)
    open('catalog-list.txt', 'w').write(out)

