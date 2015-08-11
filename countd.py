#!/usr/bin/python
import sys
from datetime import datetime
arg1=sys.argv[1]
if len(sys.argv)==2:
	currentt=datetime.now()
	arg2=currentt.strftime("%d/%m/%Y")
else:
	arg2=sys.argv[2]
def countDays(date1=arg1,date2=arg2):
	myFormat="%d/%m/%Y"
	d1=datetime.strptime(date1, myFormat)
	d2=datetime.strptime(date2, myFormat)
	nrDays=abs(d2-d1)
	print 'Between %s and %s are: %d days'%(date1,date2,nrDays.days)
countDays()
