#!/usr/bin/env python

import click

import os
import numpy as np
import pandas as pd
import re

import requests
import datetime
import requests_cache
import warnings
import traceback

from utils import *

def from_json(r):
    try:
        return r.json()
    except:
        return

def get_name(dpkg):
    try:
        return dpkg['name']
    except:
        warnings.warn(traceback.format_exc())
        return

@click.command()
@click.option('--filename_in', default="data/catalog-list.csv,data/core-list.csv", help=u"Filenames")
@click.option('--request/--no-request', default=True, help=u"Perform request")
@click.option('--validate/--no-validate', default=True, help=u"Validate")
def main(filename_in, request, validate):
    session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=datetime.timedelta(days=3))

    for filename in filename_in.split(','):
        print("Processing '%s'" % filename)
        df = process(filename, request, validate, session)
        short_filename, ext = os.path.splitext(os.path.basename(filename))
        filename_out = os.path.join("out", short_filename + ".csv")
        df.drop(["response", "datapackage", "url_raw"], axis=1, inplace=True)
        df.to_csv(filename_out, index=False)
        print(df)

def process(filename, request, validate, session):
    """
    Read a txt file and returns a DataFrame
    """
    df = pd.read_csv(filename)

    df['url_raw'] = df['url'].map(build_github_raw_url)
    df['url_optional'] = np.where(df['url_optional'].isnull(), df['url_raw'], df['url_optional'])

    if request:
        df['response'] = df['url_optional'].map(lambda url: request_dpkg(url, session))
        df['status_code'] = df['response'].map(lambda r: r.status_code)
        df['datapackage'] = df['response'].map(from_json)
        df['datapackage_name'] = df['datapackage'].map(get_name)

        print("")
        print("status_code!=200")
        print(df[df['status_code']!=200])

    if validate:
        df['valid'] = df['url_optional'].map(lambda url: is_valid(url, session)[0])
        print("")
        print("not valid")
        print(df[~df['valid']])

    return df

if __name__ == '__main__':
    main()
