#!/usr/bin/env python2.7

import sys

countries = {}
f = open('../countrycodes.csv')
for line in f:
    toks = line.split(',')
    countries[toks[3].strip()] = toks[0:2]

line = sys.stdin.next()
print line.strip() + ",country,iso"
for line in sys.stdin:
    toks = line.strip().split(',')
    try:
        print line.strip() + "," + ",".join(countries[toks[3]])
    except:
        print line.strip() + ",Unknown,?" 


