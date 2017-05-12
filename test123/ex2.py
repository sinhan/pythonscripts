#!/usr/bin/python
from sys import argv
a , b , c = argv
print "Arguments to script are %s, %s" % (b,c)
formatter = "%r %r %r"
x = 10
print "help"
print "%s is  %s"  % ("Neeraj","man")
print "Hens : ", 30
print 5 < 3 
print "=" * 20
print "there are ", x ,"cars" ,
print "there are " + str(x) + "cars"
print formatter % ("test" , "is" , "true" )
print formatter % (True, False, False )
print "a\nb\n"
print """
this
      is not a good 
format
"""
print """
\t* first
\t* secnd
"""
print "how are you" , 
x = raw_input()
print "i am also", x
print "I am also going to " + raw_input("Where are you going ? ")
print "How old are you?" , raw_input()

