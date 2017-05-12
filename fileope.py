#!/usr/bin/python

fname1=raw_input("open source file1 ?")
fname2=raw_input("open source file2 ?")
fname3=raw_input("open target file3 ?")

o=[]

try:
   file1 = open(fname1)
except IOError, e :
   print e
else :
   f1=file1.read()
   o.append(f1)

try:
   file2 = open(fname2)
except IOError, e :
   print e
else :
   f2=file2.read()
   o.append(f1)

try:
   file3 = open(fname3, 'w')
except IOError, e :
   print e
else :
   for entries in o:
     file3.write(entries)
   file3.close()
