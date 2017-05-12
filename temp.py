a = [5,7,3,4]
print a
out = []
for i,e1 in enumerate(a):
   prod = 1
   for j,e2 in enumerate(a):
      if i != j:
         prod *= e2
   out.append(prod)
print out

mult=reduce(lambda x,y: x*y, a) 
print [ mult/i for i in a ]

#b=[]
#for i in a:
#  ans=mult/i
#  b.append(ans)
#print b

#b=[]
#for i,j in enumerate(a):
#  ans=mult/a[i]
#  b.append(ans)
#print b
  
