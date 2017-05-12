#!/usr/bin/python

import os, shutil
cwd=os.getcwd()

print os.getcwd()

#os.mkdir("test")
#os.chdir("test")

print os.listdir(os.getcwd())

#os.rename("test", "test123")

scriptname=os.path.realpath(__file__)
print scriptname
print os.path.basename(scriptname)
print os.path.dirname(scriptname)

print os.path.split(scriptname)
print os.path.splitext(os.path.basename(scriptname))

path =  os.path.join(cwd,os.listdir (cwd)[0])

print path

print os.getcwd()

