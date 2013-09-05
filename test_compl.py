#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argcomplete, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--env-var1")
parser.add_argument("--env-var2")

subparsers = parser.add_subparsers( help = "subcommand help" )
p1 = subparsers.add_parser( "WOWOW" , help = "xyz" )

argcomplete.autocomplete(parser)

args = parser.parse_args()