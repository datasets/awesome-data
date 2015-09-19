import json
import time
import sys
import argparse
from bs4 import BeautifulSoup

import datetime
import requests
import requests_cache

# We'd so like not to have to scrape this and just use the API but we can't ...
# http://developer.github.com/changes/2013-10-18-new-code-search-requirements/
def get_list_from_github(session):
    url = 'https://github.com/search?l=json&q=name+resources+filename%3Adatapackage.json+path%3A%2F&type=Code'
    failuresLeft = 5

    while (True):
        response = session.get(url)
        code = response.status_code
        if response.status_code < 400:
            break
        elif code == 429:
            print('ERROR! Status code %s, sleeping for 20' % code)
            time.sleep(20)
        else:
            print('ERROR! Status code %s, exiting' % code)
            return []

    soup = BeautifulSoup(response.text)
    # total number of results
    total = int(soup.select('.selected .counter')[0].get_text().replace(',', ''))
    print('Current GitHub search returned %s results' % total)

    # do the first one to save loading again
    try:
        out = extractReposFromPage(soup)
    except ValueError:
        print('First page of results did not contain any data packages')
        failuresLeft -= 1

    # now go through results pages - 10 results per page
    ii = 2
    while failuresLeft > 0:
        slept = False
        turl = url + '&p=%s' % ii
        print('Processing: %s' % turl)

        # Retry until the request succeeds
        while True:
            response = session.get(turl)
            code = response.status_code
            if (code < 400):
                ii += 1
                break

            print('ERROR! Status code: %s, sleeping for 20' % code)
            time.sleep(20)
            slept = True

        body = response.text
        soup = BeautifulSoup(body)
        try:
            tmp = extractReposFromPage(soup)
        except ValueError:
            failuresLeft -= 1
            if failuresLeft <= 0:
                print('Got 5 pages that contained no data packages, exiting.')
                break

            continue

        out += tmp
        # sleep to prevent github getting unhappy and 420'ing us
        if not response.from_cache:
            if ii % 10 == 0 and not slept:
                print('Sleeping for 60 to avoid rate limit')
                time.sleep(60)
            else:
                time.sleep(1)

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
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', default='3', type=int,
        help='Number of searches to run')
    parser.add_argument('-H', '--hours', default='72', type=int,
        help='Number of searches to run')
    args = parser.parse_args()

    session = requests_cache.CachedSession(
        cache_name='cache', backend='sqlite',
        expire_after=datetime.timedelta(hours=args.hours))

    out = []

    for i in range(0, args.count):
        print('Starting run {0} of {1}'.format(i+1, args.count))
        out += get_list_from_github(session)

    if not out:
        print('Found no data packages, exiting')
        sys.exit(1)

    # Sort and deduplicate.
    out = sorted(set(out))
    print('Found %s data packages' % len(out))
    out = '\n'.join(out)
    open('catalog-list.txt', 'w').write(out)
