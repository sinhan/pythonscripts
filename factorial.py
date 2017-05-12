def fac1(n):
   f=1
   for i in range(1,n+1):
       f *= i
   return f

def fac2(n):
   if n == 0:
       return 1
   return n * fac2(n-1)
def fac3(n):
   if n == 0:
       return 1
   return reduce(lambda x,y: x*y, range(1,n+1))  

print  fac1(5)
print fac2(6)
print fac3(1)
