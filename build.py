import json
import urllib

def load_dataset(id_):
    print('Processing: %s' % id_)
    url = 'https://raw.github.com/datasets/' + id_ + '/master/' + \
        'datapackage.json'
    # TODO: deal with 404s gracefully
    try:
        datapackage = json.load(urllib.urlopen(url))
    except:
        print('Failed to load %s from %s' % (id_, url))
        return None
    datapackage['github_url'] = 'https://github.com/datasets/' + datapackage['name']
    for info in datapackage['files']:
        if (not info.get('url') and info.get('path')):
            info['url'] = datapackage['github_url'].replace('github.com',
                    'raw.github.com') + '/master/' + info['path']
    return datapackage

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

