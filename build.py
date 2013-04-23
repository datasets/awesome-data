import json
import urllib2
try:
    from markdown import markdown
except ImportError:
    print('WARNING: failed to import markdown')
    markdown = lambda x: x

def load_dataset(datapackage_url):
    print('Processing: %s' % datapackage_url)
    base = datapackage_url.rstrip('datapackage.json')
    # TODO: deal with 404s gracefully
    try:
        datapackage = json.load(urllib2.urlopen(datapackage_url))
    except:
        print('Failed to load %s' % datapackage_url)
        return None

    # ensure certain fields exist
    if not 'description' in datapackage:
        datapackage['description'] = ''

    # get the readme
    readme_url = base + 'README.md'
    try:
        readmefo = urllib2.urlopen(readme_url)
        datapackage['readme'] = readmefo.read().replace('\r\n', '\n')
    except:
        datapackage['readme'] = datapackage['description']
        pass
    # set description as first paragraph of readme if we no description
    if not datapackage['description'] and 'readme' in datapackage:
        # first extract plain text ...
        html = markdown(unicode(datapackage['readme'], 'utf8'))
        plain = strip_tags(html).split('\n\n')[0].replace(' \n', '').replace('\n', ' ')
        datapackage['description'] = plain.encode('utf8')

    for info in datapackage['resources']:
        if (not info.get('url') and info.get('path')):
            info['url'] = base + info.get('path')

    return datapackage

from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_endtag(self, tag):
        if tag == 'p':
            self.fed.append('\n\n')
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def load(dataset_names):
    out = [ load_dataset(name) for name in dataset_names if name ]
    # if failed loads returned dp is None
    out = [ x for x in out if x ]
    out = dict([ (x['name'], x) for x in out ])
    return out


def build_index(dataset_list_url, outpath='dp-index.json'):
    dataset_list = open(dataset_list_url).read().split('\n')
    # strip out blank lines or similar which can creep in
    dataset_list = [_to_dp_url(ds) for ds in dataset_list if ds]
    index = load(dataset_list)
    with open(outpath, 'w') as dest:
        json.dump(index, dest, indent=2, sort_keys=True)

def _to_dp_url(nameOrUrl):
    if '/' not in nameOrUrl:
        url = 'https://raw.github.com/datasets/' + nameOrUrl + '/master/'
    else:
        url = nameOrUrl

    if not url.endswith('datapackage.json'):
        url = url.rstrip('/')
        url += '/datapackage.json'

    return url
        


import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        listpath = sys.argv[1]
    else:
        listpath = 'list.txt'
    if len(sys.argv) > 2:
        outpath = sys.argv[2]
    else:
        outpath = 'dp-index.json'
    build_index(listpath, outpath)

