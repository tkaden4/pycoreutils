#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2009, 2010, 2011 Hans van Leeuwen.
# See LICENSE.txt for details.

from __future__ import print_function, unicode_literals
import pycoreutils


@pycoreutils.addcommand
def sh(p):
    p.set_defaults(func=func)
    p.description = "Start a shell"


def func(args):
    return pycoreutils.PyCoreutils().cmdloop(pycoreutils.showbanner(width=80))
