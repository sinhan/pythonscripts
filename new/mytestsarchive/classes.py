#!/usr/bin/python

class my_class(object):
   'this is my_class'
   def __init__(self, ab):
       self.ab= ab

   def print_info(self):
       print self.ab

       
       
b = my_class("Happy birthday to you")
b.print_info()
       
