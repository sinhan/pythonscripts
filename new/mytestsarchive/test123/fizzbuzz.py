#!/usr/bin/python

for i in range(1,101):
    if i%3 == 0 and i%5 == 0 : 
       print str(i)  + "LinkedIn"
    elif  not i%3 :
       print str(i) + "Linked"
    elif not i%5 :
       print str(i)+ "In"

for i in range(101,151):
    mystring = ""
    if (i%3 == 0): mystring += "Linked"
    if (i%5 == 0): mystring += "In"
    print str(i) + mystring

for i in range(151,201):
    x=(not i%3) * "Linked"
    y=(not i%5) * "In"
    if y or x:
      print str(i) + x+y


