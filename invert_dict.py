#!/usr/bin/python

dict1={
        "FB" : 12 ,
        "GO" : 3 , 
        "WM" : 30 , 
        "Ap" : 50 ,
        "BAp" : 150
      }

for x in dict1:
   #print x + ":" + int(dict1[x]) 
   print "%s : %d"  % (x, int(dict1[x])) 

print "===" * 8
i_dict1={v: k for k, v in dict1.iteritems()}
for x in i_dict1:
   print "%s : %s"  % (x, i_dict1[x]) 

print "===" * 8
mini = min(zip(i_dict1.keys(), i_dict1.values()))
print mini

maxi = max(zip(dict1.values(), dict1.keys()))
print maxi


print "===" * 8
print sorted(zip(dict1.values(), dict1.keys()), reverse=True)
