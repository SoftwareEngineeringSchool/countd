#!/usr/bin/python

import sys
from datetime import datetime

arguments=sys.argv[1:]
if "-f" in arguments:
	format=sys.argv[2]
else:
	format="%d/%m/%Y"
arg2=sys.argv[len(sys.argv)-1]
if len(sys.argv) in [3,5]:
	arg1=sys.argv[len(sys.argv)-2]
else:
	currentt=datetime.now()
	arg1=currentt.strftime(format)

def countDays(formatd=format,date1=arg1,date2=arg2):
	myFormat=formatd
	d1=datetime.strptime(date1, myFormat)
	d2=datetime.strptime(date2, myFormat)
	nrDays=abs(d2-d1)
	print 'Between %s and %s are: %d days'%(date1,date2,nrDays.days)

countDays()
