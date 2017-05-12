def isprime(n):
   if n==1:
      return False
   for x in range(2,n):
      if n%x==0:
         return False
   return True

print [ n for n in range(1,100) if isprime(n) ]
a=1
b=0
while b<101:
  if isprime(a):
     print a,
     b +=1  
  a +=1
   
   
