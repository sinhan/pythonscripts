with open("mywords") as f:
  words=f.read()

print words

splitwords=words.split()

d={}.fromkeys(splitwords,0)
for w in splitwords:
    d[w] += 1
print d
#for keys in d:
#  print keys, d[keys]

#------------------------------------------------
ans = dict((c,splitwords.count(c)) for c in splitwords)
print ans
ans1 = dict((c,words.count(c)) for c in words)
print ans1


#------------------------------------------------
a = [10,30,50,70,70,30,40,30,10,20,10,20,25,30]

#------------------------------------------------
import collections
b = collections.Counter(a)
print b
print [ (k,v) for k,v in b.items() if v > 1 ]
print [ (k,v) for k,v in b.most_common(5) ]

for k,v in sorted(b.items(), key=lambda x: x[1], reverse=True):
#for x,y in sorted(dicti.items(), key=lambda v: v[1] )
   print k, "#" * v

#------------------------------------------------
d = {}
for k in a:
   d[k] = 0
for k in a:
   d[k] += 1

print [k for k,v in d.items() if v > 1]
#------------------------------------------------
d = {}
for k in a:
    d[k] = d.get(k,0) + 1
print [k for k,v in d.items() if v > 1]
