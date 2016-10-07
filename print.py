#!/usr/bin/python

from colored import fg, attr
import sys

ip = str(sys.argv[1])

print '\nYour IP : %s %s %s\n' % (fg(84), ip, attr(0))
