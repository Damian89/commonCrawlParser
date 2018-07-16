#!/usr/bin/env python
# coding: utf8

import argparse


def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d", "--domain",
        help="domain",
        type=str,
        dest="domain",
        default=None,
        required=True
    )
    parser.add_argument(
        "-o", "--outfile",
        help="Path to save the output",
        type=str,
        dest="outfile",
        required=True

    )
    parser.add_argument(
        "-i", "--index",
        nargs="?",
        type=str,
        action="append",
        help="Use only this index",
        dest="index_used",
        default=None
    )
    args = parser.parse_args()

    return args.domain, args.outfile, args.index_used
