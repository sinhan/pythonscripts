words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']
d1={}

for w in words:
  d1[w]=''.join(sorted(w))

print d1
d2={}

for k,v  in d1.items():
   d2.setdefault(v,[]).append(k)
print d2

for v in d2.values():
  print v
