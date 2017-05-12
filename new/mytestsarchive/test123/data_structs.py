#!/usr/bin/python
from collections import Counter 
a = [ 1, 2, 1, 5, 4, 3, 4, 8, 7, 4, 6, 8, 9 ]

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}


tuple_list=[('eyes', 8), ('the', 5), ('look', 4), ('into', 3), ('my', 3), ('around', 2), ("you're", 1), ("don't", 1), ('under', 1), ('not', 1)]

def remove_dups(seq, key=None):
   seen=set()
   for i in seq:
     val=i if key is None else key(item)
     if val not in seen:
       yield i
       seen.add(val)
x = list(remove_dups(a))
print x
   
word_counts=Counter(words)
print word_counts['eyes']
top = word_counts.most_common()
print top

for i,j in top:
   print "%s : %d" % (i,j) 

ab=( n for n in a if n%2 )
for abc in ab:
 print(abc)

def isodd(m):
  if m%2:
     return m

print isodd(11111)

odds=list(set(filter(isodd, a)))
print odds

p1 = { k: v for k,v in prices.items() if v > 200 }
print p1

sums = sum( x * x for x in a )  
print sums

sv = ('ACME', 50, 123.45)
print(",".join(str(s) for s in sv))
