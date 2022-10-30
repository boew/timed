#!/bin/bash
LOGFILE=/home/boe/timed/bk/bbk.log
/usr/bin/bbk_cli --out=$LOGFILE >> unexpected.log.txt 2>&1

