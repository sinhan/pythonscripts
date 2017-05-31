a=[1, 2, 3, 5, 8, 9, 10 ]
b=[11, 1, 4, 3, 6, 9, 10 ]

c = a + b
c= list(set(c))
print c

L = [5,3,7,9,5,1,4,7]
newL = []
[newL.append(v) for v in L if newL.count(v) == 0]
# or [newL.append(v) for v in L if v not in newL]
print newL
