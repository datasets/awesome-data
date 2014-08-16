Register (list) of Data Packages including the core datasets in the
Frictionless Data Project.

Currently two registers maintained here:

* catalog-list.txt - catalog of all the community data packages we can find (at
  the moment largely those found on github via automatic search)
* core-list.txt - ["Core" Datasets][core] (hand-maintained)

[core]: http://data.okfn.org/roadmap/core-datasets

## Preparation

### Catalog List

The main Catalog list is scraped using the python script `scripts/scrape.py`:

    # install deps
    pip install -r scripts/requirements.txt
    # scrape data
    python scripts/scrape.py

Note we'd prefer not to scrape and use the API but we can't do the relevant
query via the API - see
<http://developer.github.com/changes/2013-10-18-new-code-search-requirements/>

### Core List

To add a dataset please add it to the `core-list.txt` - we recommend
fork and pull.

Discussion of proposals for new datasets and for incorporation of prepared
datasets takes place in the [issues][].

To **propose a new dataset for inclusion**, please create a [new
issue](https://github.com/datasets/registry/issues/new).

[issues]: https://github.com/datasets/registry/issues

