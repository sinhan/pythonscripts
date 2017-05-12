def fibi(n):
  a,b=0,1
  for i in range(n):
     a,b=b,a+b
  return a

def fibr(n):
   if n==0 or n == 1: return n
   return fibr(n-1) + fibr(n-2)

def fibg(n):
  a,b=0,1
  for i in range(n):
     yield a
     a,b=b,a+b

for i in range(10):
   print (fibi(i), fibr(i)) 

for item in fibg(10):
   print(item),



