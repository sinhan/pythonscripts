#!/usr/bin/python
from sys import argv

def print_args(*argso):
   arg1 ,  arg2 = argso 
   print "Arguments are : %s and %s" % (arg1 , arg2)

def print_all_args(*args):
#   for arg in args:
#      if arg is not None:
#         print "Now my argument is : " , arg
   return args
#   return True

print_args("one" , "two") 
print print_all_args("test", "my", "something" , "that " , "is" , "working")


