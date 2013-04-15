import json
import urllib2

def load_dataset(id_):
    print('Processing: %s' % id_)
    base = 'https://raw.github.com/datasets/' + id_ + '/master/'
    url = base + 'datapackage.json'
    # TODO: deal with 404s gracefully
    try:
        datapackage = json.load(urllib2.urlopen(url))
    except:
        print('Failed to load %s from %s' % (id_, url))
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
        import markdown
        html = markdown.markdown(unicode(datapackage['readme'], 'utf8'))
        plain = strip_tags(html).split('\n\n')[0].replace(' \n', '').replace('\n', ' ')
        datapackage['description'] = plain.encode('utf8')

    # some final tidying up
    datapackage['github_url'] = 'https://github.com/datasets/' + datapackage['name']
    for info in datapackage['resources']:
        if (not info.get('url') and info.get('path')):
            info['url'] = datapackage['github_url'].replace('github.com',
                    'raw.github.com') + '/master/' + info['path']

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
    out = dict([ (x['name'], x) for x in out ])
    return out


def build_index():
    dataset_list_url = 'list.txt'
    dataset_list = open(dataset_list_url).read().split('\n')
    # strip out blank lines or similar which can creep in
    dataset_list = [ds for ds in dataset_list if ds]
    index = load(dataset_list)
    with open('index.json', 'w') as dest:
        json.dump(index, dest, indent=2, sort_keys=True)

if __name__ == '__main__':
    build_index()

