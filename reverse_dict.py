dict1={ "SF" : "US" , "LA" : "US", "LONDON" : "UK", "DEL" : "IND" }

dict2={v:k for k,v in dict1.iteritems()}
print dict2 

#from collections import defaultdict

#d1 = defaultdict(list)
#for k,v in dict1.items():
#    d1[v].append(k)
#print d1

d2 = {}
for k,v in dict1.items():
       d2.setdefault(v,[]).append(k)
print d2
