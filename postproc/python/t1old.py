#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#https://pypi.org/project/pulsectl/

def main(benchlogfile="~/timed/postproc/modlog2019-11-28.txt")
state = None
lineStarts = {
   '==': 'entry',
   'https': 'site',
   'FINISHED': 'finished',
   'Total': 'clock',
   'Downloaded': 'dld'}
with open(benchlogfile, 'r') as blf:
    for line in blf:
        if (match
        
