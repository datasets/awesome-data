# -*- coding: utf-8 -*-
# vim:sts=4:ts=4:sw=4:expandtab

import argparse
import json
import sys
import urllib
import webbrowser

def coloured(msg, col):
    colours = {
        'green': '\033[00;32m',
        'red': '\033[00;31m',
        'reset': '\033[0m'
    }

    if not col in colours:
        raise ValueError('Unsupported colour "%s"' % col)

    return colours[col] + msg + colours['reset']

def validate(url):
    validator = 'http://data.okfn.org/tools/validate'
    param = urllib.urlencode({ 'url': url })
    urlo = urllib.urlopen(validator + '.json?' + param)

    data = json.load(urlo)

    if (data['valid'] and args.invalid) or (not data['valid'] and args.valid):
        return

    if args.quiet:
        print(url)
    elif data['valid']:
        print('[ %s ] ' % coloured('OK', 'green') + url)
    else:
        print('[%s] ' % coloured('FAIL', 'red') + url)
        print('    URL: ' + validator + '?' + param)

        if args.open:
            webbrowser.open(validator + '?' + param)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--open', action='store_true',
        help='open failing validator URLs in a web browser')
    parser.add_argument('-q', '--quiet', action='store_true',
        help='with --valid or --invalid, only print the data package\'s URL')

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--valid', action='store_true',
        help='only print data packages that pass validation')
    mode.add_argument('--invalid', action='store_true',
        help='only print data packages that fail validation')
    args, rest = parser.parse_known_args()

    if args.quiet and not (args.valid or args.invalid):
        sys.stderr.write('warning: --quiet has no effect without --valid or'
            ' --invalid\n')
        args.quiet = None

    for arg in rest:
        with open(arg, 'r') as fh:
            for line in fh:
                validate(line.rstrip('\n'))
