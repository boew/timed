#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#https://pypi.org/project/pulsectl/

import re

class LogProc:
    def __init__(self,
                 infile = "/home/boe/timed/postproc/shortpythonlog.txt",
                 outfile = "/home/boe/timed/postproc/shortpythonlogOUT.txt"):
        self._lineStarts = {
            '==': self._entry,
            'ht': self._site,
            'FI': self._finished,
            'To': self._clock,
            'Do': self._dld}
            
        with open(infile, 'r') as inf:
            with open(outfile, 'a') as outf:
                for self._line in inf:
                    if (self._line[:2] in self._lineStarts):
                        #print('line:', self._line[:2])
                        #print('starts:', self._lineStarts[self._line[:2]])
                        toWrite = self._lineStarts[self._line[:2]]()
                        #print(toWrite)
                        outf.write(toWrite)
                outf.write('\n')
                
    def _entry(self):
        return ('\n')
    
    def _site(self):
        m = re.search(r'\.(.*)\.', self._line)
        if (m): 
            return ('\t' + m.group(1))


    def _finished(self):
        #FINISHED --2017-03-04 17:30:21--        
        m = re.match(r'FINISHED --(.+)--', self._line)
        if (m): 
            return ('\t' + m.group(1))
        
    def _clock(self):
        #Total wall clock time: 19s
        m = re.match(r'Total wall clock time:((.+)m)?((.+)s)?', self._line)
        #print(self._line)
        #print(minutes, seconds)
        #print(m)
        if (m):
            minutes = m.group(2) or ""
            seconds = m.group(4) or ""
            #print(m)
            return ('\t' + minutes + '\t' + seconds)
        else:
            return('Broken')
        
    def _dld(self):
        #Downloaded: 68 files, 4.6M in 1.1s (34.4 Mb/s)
        m = re.match(r'Downloaded: (\d+) files, ([.\d]+)(M|K) in ((.+)m)?((.+)s)? .([.\d]+) (M|K)b/s.', self._line)
        if (m): 
            minutes = m.group(5) or ""
            seconds = m.group(7) or ""
            return ('\t' + m.group(1) +
                    '\t' + m.group(2) +
                    '\t' + m.group(3) +
                    '\t' + minutes +
                    '\t' + seconds +
                    '\t' + m.group(8) +
                    '\t' + m.group(9))

if ('__main__' == __name__):
    #myLP = LogProc()
    myLP = LogProc(infile = "/home/boe/timed/postproc/orglog2019-11-28.txt",
                 outfile = "/home/boe/timed/postproc/python/outlog2019-11-28.txt")

    
