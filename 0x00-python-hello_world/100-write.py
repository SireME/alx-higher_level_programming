#!/usr/bin/python3

import sys


def syswrite(wr):
    sys.stderr.write(wr)


text = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
syswrite(text)
sys.exit(1)
