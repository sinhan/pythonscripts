#!/usr/bin/python

def ispalin(x):
   for i,ch in enumerate(x):
      if ch != x[-i-1]:
         print "No a palindrome"
         return "False"
   print "A palidrome"
   return True

def ispalin1(x):
   print("Is a palidrome" if x == x[::-1] else "not a palidrome")

while True:
   try:
      x =  raw_input("Type a string > ")
      x=x.strip()
      ispalin1(x) 
   except (KeyboardInterrupt, EOFError):
      print "good bye"
      break

