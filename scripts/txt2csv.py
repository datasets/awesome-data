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

def get_user_project(url):
    """
    Returns a tuple (user, project) from a GitHub URL
    """
    pattern = "https:\/\/github.com\/(.*)\/(.*)"
    m = re.match(pattern, url)
    if m is not None:
        (user, project) = m.groups()
        return user, project
    return '', ''

def build_github_url(user, project, branch='master'):
    """
    Returns a GitHub URL from user, project and branch
    branch can be, for example 'master' but it can also be 'gh-pages'
    """
    return "https://raw.githubusercontent.com/%s/%s/%s/" % (user, project, branch)


def request_dpkg(url, session):
    return session.get(url + 'datapackage.json')

def is_valid(url, session):
    """
    Return tuple (valid, errors) to know if url is a valid DataPackage
    """
    url_api_base = 'http://data.okfn.org'
    endpoint = '/tools/validate.json'
    try:
        response = session.get(url_api_base + endpoint, params={'url': url})
        resp = response.json()
        return resp['valid'], resp['errors']
    except:
        return False, traceback.format_exc()

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
@click.option('--filename-in', default="catalog-list.txt,core-list.txt", help=u"Filenames")
@click.option('--request/--no-request', default=False, help=u"Status code")
@click.option('--validate/--no-validate', default=False, help=u"Validate")
def main(filename_in, request, validate):
    session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=datetime.timedelta(days=3))

    cols = ['url', 'owner', 'name', 'url_optional']
    #cols = ['url', 'owner', 'name', 'status_code', 'valid']

    for filename in filename_in.split(','):
        print("Processing '%s'" % filename)
        df = process(filename, request, validate, session)
        filename, ext = os.path.splitext(filename)
        filename_out = filename + ".csv"
        df = df[cols]
        df.to_csv(filename_out, index=False)
        print("")

def process(filename_in, request, validate, session):
    """
    Read a txt file and returns a DataFrame
    """
    df = pd.read_csv(filename_in, names=['url'])
    s_user_project = df['url'].map(get_user_project)
    df['user'] = s_user_project.map(lambda t: t[0])
    df['project'] = s_user_project.map(lambda t: t[1])
    df['branch'] = 'master'
    df['url_optional'] = ''

    df['url_branch'] = df.apply(
        lambda row: build_github_url(
            row['user'], row['project'], row['branch']), axis=1)

    if request:
        df['response'] = df['url_branch'].map(lambda url: request_dpkg(url, session))
        df['status_code'] = df['response'].map(lambda r: r.status_code)
        df['datapackage'] = df['response'].map(from_json)
        df['datapackage_name'] = df['datapackage'].map(get_name)

        print("")
        print("status_code!=200")
        print(df[df['status_code']!=200])

    if validate:
        df['valid'] = df['url_branch'].map(lambda url: is_valid(url, session)[0])
        print("")
        print("not valid")
        print(df[~df['valid']])

    df['name'] = np.where(df['datapackage_name']!=df['project'], df['datapackage_name'], '')
    df['owner'] = df['user']

    return df


if __name__ == '__main__':
    main()
