#!/usr/bin/python
from sys import argv
a , b  = argv
print "Arguments to script are %s, %s" % (a,b)
#x = open(b)
#xd =  x.read()
#print x.read()
#print x.readline()
#print x.readlines()

x = open(b)
y = open("abcd", 'w')
#for lines in x:
    #print lines
#     y.write(lines,)

#y.write(xd)
y.write(x.read())
x.close()
y.close()
#!/usr/bin/python
from sys import argv
a , b  = argv
print "Arguments to script are %s, %s" % (a,b)
#x = open(b)
#xd =  x.read()
#print x.read()
#print x.readline()
#print x.readlines()

x = open(b)
y = open("abcd", 'w')
#for lines in x:
    #print lines
#     y.write(lines,)

#y.write(xd)
y.write(x.read())
x.close()
y.close()
