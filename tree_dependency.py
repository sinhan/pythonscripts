import time
d1={ 'a' : ['b','c','f'],
     'b' : ['c','d'],
     'e' : [],
     'f' : ['c','e','i'],
     'g' : ['h','f'],
     'i' : ['f']
   }
myd={ 'a' : ['b'],
      'b' : ['c'],
      'c' : ['d','a']
    }

def resolve(arg):
    #d=dict((k, set(arg[k])) for k in arg)
    d=dict(arg)
    r=[]
    while d:
        print "---" * 8
        # values not in keys (items without dep)
        t=set(i for v in d.values() for i in v)-set(d.keys())
        # and keys without value (items without dep)
        t.update(k for k, v in d.items() if not v)
        #r.append(t)
        r.extend(list(t))
        print r
        # and cleaned up
        d2=dict(d)
        d=dict(((k, set(v)-t) for k, v in d.items() if v))
        if d2 == d:
            print d
            #raise Exception('Circular reference detected. Will not able to resolve further')
            raise SystemExit('Circular reference detected. Will not able to resolve further')
        time.sleep(2)

    return r

if __name__=='__main__':
    #print resolve(d1)
    #resolve(d1)
    resolve(myd)
