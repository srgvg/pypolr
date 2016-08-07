#!/usr/bin/env python

from __future__ import print_function
import sys
import requests


POLR_API_KEY = 'blah'
POLR_URL_BASE = 'https://polr.me'
POLR_API_BASE = '/api/v2/'

POLR_API_URL = POLR_URL_BASE + POLR_API_BASE


def eprint(*args, **kwargs):
    ''' Print to stderr '''

    print(*args, file=sys.stderr, **kwargs)


def polr_action(api_action_url, api_key, api_parameters):
    '''
    Execute an action request on the Polr Api
    http://docs.polr.me/en/latest/developer-guide/api/#actions
    '''

    params = dict(key=api_key)
    params.update(api_parameters)

    return requests.get(api_action_url, params=params)


def polr_action_lookup(api_base, api_key, url_ending, url_key=None):
    '''
    Execute a lookup action request on the Polr Api
    '''

    api_action_url = api_base + 'action/lookup'

    params = dict(url_ending=url_ending)
    if url_key:
        params.update(dict(url_key=url_key))

    req = polr_action(api_action_url, api_key, params)
    return req.status_code, req.text


def polr_action_shorten(api_base, api_key, url, is_secret=False, custom_ending=None):
    '''
    Execute a shortening action request on the Polr Api
    '''

    api_action_url = api_base + 'action/shorten'

    params = dict(url=url, is_secret=is_secret)
    if custom_ending:
        params.update(dict(custom_ending=custom_ending))

    r = polr_action(api_action_url, api_key, params)
    return r.status_code, r.text


if __name__ == "__main__":

    ret, text = polr_action_shorten(POLR_API_URL, POLR_API_KEY, 'https://mail.google.com/', False, 'gmail')
    if ret == 200:
        print (text)
        sys.exit(0)
    else:
        eprint (text)
        sys.exit(1)

    #ret, text = polr_action_lookup(POLR_API_URL, POLR_API_KEY, '0')

