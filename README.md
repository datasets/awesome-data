Register (list) of the published datasets in the Datasets Project.

## Adding a Dataset to the Registry

To add a dataset please add it to the list.txt - we recommend fork and pull.

## Propose Datasets for Addition

Discussion of proposals for new datasets and for incorporation of prepared datasets takes place in the [issues][].

To **propose a new dataset for inclusion**, please create a [new issue](https://github.com/datasets/register/issues/new).

There is also an existing spreadsheet list of [proposed datasets for inclusion in the Datasets Project]

[issues]: https://github.com/datasets/register/issues

# For Maintainers

To build the dp-index.json (consolidating cache):

    # install markdown library if you have not already
    # then
    # optional path is location to write dp-index.json to
    python build.py [path]

