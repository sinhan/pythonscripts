def sort1(a):
    sorted=False
    while not sorted:
       sorted=True
       for i in range(len(a)-1):
          if a[i] > a[i+1]:
             sorted=False
             a[i],a[i+1]=a[i+1],a[i]
       print a, sorted

def bsort(a):

   for i in range(len(a)-1):
      for i in range(len(a)-1):
          if a[i] > a[i+1]:
              a[i],a[i+1]=a[i+1],a[i]
      print a

a=[3,1,5,7,6,4,2,8,10,9]
b=[3,1,5,7,6,4,2,8,10,9]
c=[3,1,5,7,6,4,2,8,10,9]
sort1(a)
print "=" * 8
bsort(b)
print "=" * 8
print sorted(c)

       
