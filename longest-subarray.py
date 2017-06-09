a= [1, 2, 3, 3, 2, 4 ,6, 7, 9, 6]
print a

def lis(ar):
  b={}
  b[1] = 1
  n=len(ar)
  for i in range(2,n):
    if ar[i] > ar[i-1]:
       b[i]=b[i-1] + 1
    else:
       b[i] = 1

  x=sorted(b.items(), key = lambda x : x[1] , reverse=True)[0]
  #print x
  #start=x[0]-x[1]+1
  #end=x[0]
  #print ar[start:end+1]
  p,l = x[0],x[1]
  print ar[p-l+1:p+1]

#print subarray(a)
lis(a)
~
