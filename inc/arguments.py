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
        "-t", "--threads",
        help="Threads",
        type=int,
        dest="threads",
        default=5
    )

    parser.add_argument(
        "-f", "--filter",
        nargs="?",
        type=str,
        action="append",
        help="Words to filter indices for",
        dest="filter",
        default=None
    )
    args = parser.parse_args()

    return args.domain, args.outfile, args.threads, args.filter
