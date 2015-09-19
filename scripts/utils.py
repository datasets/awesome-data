#!/usr/bin/env python

import re
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

def build_github_raw_url(url_repository, branch='master'):
    """
    Returns a GitHub "raw" URL from a repository URL
    """
    user, project = get_user_project(url_repository)
    return build_github_url(user, project, branch)

def request_dpkg(url, session):
    """
    Returns response when querying a datapackage
    """
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
