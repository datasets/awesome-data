Register (list) of Data Packages including the core datasets in the
Frictionless Data Project.

Currently two registers maintained here:

* datapackage-list.txt - ["Core" Datasets][core] (hand-maintained)
* github-list.txt - community data packages found on github (automatically)

[core]: http://data.okfn.org/roadmap/core-datasets

## Preparation

### Github List

Github list is scraped using the script `scripts/scrape.js`:

    # install deps
    npm install .
    # scrape data
    node scripts/scrape.js

Note we'd prefer not to scrape and use the API but we can't do the relevant
query via the API - see
<http://developer.github.com/changes/2013-10-18-new-code-search-requirements/>

### Core List

To add a dataset please add it to the `datapackage-list.txt` - we recommend
fork and pull.

Discussion of proposals for new datasets and for incorporation of prepared
datasets takes place in the [issues][].

To **propose a new dataset for inclusion**, please create a [new
issue](https://github.com/datasets/registry/issues/new).

[issues]: https://github.com/datasets/registry/issues

