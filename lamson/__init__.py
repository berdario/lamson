#!/usr/bin/env python

from modargs import args
from lamson import commands
import sys

def _main():
    args.parse_and_run_command(sys.argv[1:], commands, default_command="help")


