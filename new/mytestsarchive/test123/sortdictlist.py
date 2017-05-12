#!/usr/bin/python

nums=[]
for x in range(1,10):
   nums.append(x)

print nums[5]

print len(nums)

nums.append(22)

print len(nums)
print "=======" * 6
print nums

print nums.pop(-1)
print nums.pop()
print nums.pop(0)
print nums
print "=======" * 6

print nums[-1]
print nums

print "-".join(str(y) for y in nums)
print "-".join(map(str,nums))

z=["one","two","three"]

print "====".join(z)

for a in z:
   print a

for s in list(reversed(z)):
   print s
print "--" * 8
gh=z[::-1]
kl=reversed(z)

for s in gh:
   print s 
print "--" * 8
for s in kl:
   print s

print "----" * 8

for i,s in enumerate(z):
   print i + 1 ,s

print "--" * 8
for i,j in zip(z,gh):
   print('%s - %s' %(i,j))

print "--" * 8
zy=[1,2,3,4]
zy.reverse()
print zy
print type(z) 
#for s in rev:
#   print s

print "--" * 8
print nums[0:1]
print nums[0:]
print nums[0:3:-1]
print nums[-5:-2:1]

dicti={'neeraj' : 'sinha', 'maneesha' : 'dayal', 'daksh' : 'sonha', 'vinod' : 'sinha'}
print dicti['maneesha']

for x in dicti:
  print x , dicti[x] 

for key in sorted(dicti.keys()):
   print "%s : %s"  % (key,dicti[key])
print "--" * 10
for x,y in sorted(dicti.items(), key=lambda v: v[1] ):
   #print "%s : %s"  % (x,dicti[x])
   print "%s : %s"  % (x,y)
