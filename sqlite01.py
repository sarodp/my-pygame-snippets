#!/usr/bin/python

import sqlite3

mydb1 = '/home/pi/mydb01.db'
cn1 = sqlite3.connect(mydb1)

sql1 = 'select * from tb01'
cursor1 = cn1.execute(sql1)
tb01 = cursor1.fetchall()

sql2 = 'select * from tb02'
cursor2 = cn1.execute(sql2)
tb02 = cursor2.fetchall()

print "\nTest read table from sqlite3."

print "Database file:", mydb1
print "-----------------------------------"
print "\nQuery:",sql1
print  "  no.of rows = %i" % (len(tb01)),
i=0
for xrowi in tb01: 
	i =i+1  
	print "\n row(%i).data = |" % (i),
	for xdati in xrowi:
		print " %s |" % (xdati),

print "\n\nQuery:",sql2
print  "  no.of rows = %i" % (len(tb02)),
i=0
for xrowi in tb02: 
	i =i+1  
	print "\n row(%i).data = |" % (i),
	for xdati in xrowi:
		print " %s |" % (xdati),

	#print " row(%i).list => %s" % (i,xrowi)

cursor1.close
cursor2.close
cn1.close()
