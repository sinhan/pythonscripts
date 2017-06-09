a= [1, 2, 1, 2, 3, 3, 2, 4 ,6, 7, 9, 6, 2, 3, 6, 7, 8 ]
print a

def lis(ar):
  b={}
  b[0] = 1
  n=len(ar)
  for i in range(1,n):
    if ar[i] > ar[i-1]:
       b[i]=b[i-1] + 1
    else:
       b[i] = 1

  l = max(b.values())
  pos = [k for k, v in b.items() if v == l]
  print l,
  print pos
  for p in pos:
    print ar[p-l+1:p+1]

lis(a)
