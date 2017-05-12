#!/usr/bin/python
import os, subprocess
import shutil

os.system("ls -l")
print "#####" * 6
subprocess.call(["ls", "-l"])

subprocess.check_output('ls -l' , shell=True)
x = "sysadmin.py"
p = subprocess.Popen(['cat', x], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#p = subprocess.Popen(['touch'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
stdout, stderr = p.communicate()

p.wait()
#print stdout.decode('utf-8')
print stdout, stderr

data=os.popen('uname -a').read()
print data
