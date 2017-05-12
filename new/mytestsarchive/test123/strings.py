#!/usr/bin/python
import re
import os

line = 'asdf fjdk; afed, fjek,asdf, foo'
filename='abcd.txt'

line1=re.split(r'[,;\s]\s*',line)
line2=re.split(r'(?:,|;|\s)\s*',line)

print line1
print line2
print filename.startswith('ab')
print filename.startswith('b')
print filename.endswith('txt')
listoffiles=os.listdir('.')
print listoffiles
#nonpython=[ x for x in listoffiles if not x.endswith(('.py','.pyc')) ]
nonpython=( x for x in listoffiles if not x.endswith(('.py','.pyc')) )
for y in nonpython:
  print y
