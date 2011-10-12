#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2010, 2011 Hans van Leeuwen.
# See LICENSE.txt for details.

from __future__ import print_function, unicode_literals
import pycoreutils
import random
import sys


@pycoreutils.addcommand
def shuf(p):
    p.set_defaults(func=func)
    p.description = "Write a random permutation of the input lines to " +\
                    "standard output."
    p.usage = '%(prog)s [OPTION]... [FILE]\nor:    %(prog)s -e [OPTION]... ' +\
              '[ARG]...\nor:    %(prog)s -i LO-HI [OPTION]...'
    p.add_argument('file', nargs='?')
    p.add_argument("-e", "--echo", action="store_true", dest="echo",
            help="treat each ARG as an input line")
    p.add_argument("-i", "--input-range", dest="inputrange",
            help="treat each number LO through HI as an input line")
    p.add_argument("-n", "--head-count", dest="headcount",
            help="output at most HEADCOUNT lines")
    p.add_argument("-o", "--output", dest="output",
            help="write result to OUTPUT instead of standard output")


def func(args):
    lines = ''
    outfd = sys.stdout

    # Write to file if -o is specified
    if args.output:
        outfd = open(args.output, 'w')

    if args.echo:
        if args.inputrange:
            pycoreutils.StdErrException(
                        "{0}: cannot combine -e and -i options".format(prog))

        lines = args.file
        random.shuffle(lines)

        if args.headcount:
            lines = lines[0:int(args.headcount)]
        for line in lines:
            outfd.write(line + '\n')

    elif len(args) > 1:
        raise pycoreutils.ExtraOperandException(prog, args[1])

    elif args.inputrange:
        (lo, hi) = args.inputrange.split('-')
        lines = list(range(int(lo), int(hi) + 1))
        random.shuffle(lines)

        if args.headcount:
            lines = lines[0:int(args.headcount)]
        for line in lines:
            outfd.write(line + '\n')

    else:
        # Use stdin for input if no file is specified
        if len(args) == 0:
            fd = sys.stdin
        else:
            fd = open(args[0])

        lines = fd.readlines()
        random.shuffle(lines)

        if args.headcount:
            lines = lines[0:int(args.headcount)]
        for line in lines:
            outfd.write(line)
