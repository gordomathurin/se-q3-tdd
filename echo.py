#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Gordon Mathurin"


import sys
import argparse

"""
positional arguments:
        text         text to be manipulated

    optional arguments:
        -h, --help   show this help message and exit
        -u, --upper  convert text to uppercase
        -l, --lower  convert text to lowercase
        -t, --title  convert text to titlecase

"""


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    # your code here
    paser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    paser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')

    paser.add_argument(
        '-l', '--lower', help='convert text lowercase', action='store_true')

    paser.add_argument(
        '-t', '--title', help='convert text titlecase', action='store_true')

    paser.add_argument('text', help='text to be manipulated')
    return paser


def main(args):
    """Implementation of echo"""
    # your code here
    # Conditionals here if upper do this, if lower do that
    paser = create_parser()
    ns = paser.parse_args(args)

    text = ns.text
    print(text)

    if not ns:
        paser.print_usage()
        sys.exit(1)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
