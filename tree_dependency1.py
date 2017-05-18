def dep(arg):
    d=dict((k, set(arg[k])) for k in arg)
    print d
    r=[]
    while d:
        # values not in keys (items without dep)
        t=set(i for v in d.values() for i in v)-set(d.keys())
        # and keys without value (items without dep)
        t.update(k for k, v in d.items() if not v)
        print t
        # can be done right away
        r.append(t)
        # and cleaned up
        d=dict(((k, v-t) for k, v in d.items() if v))
    return r

if __name__=='__main__':
    d=dict(
        a=('b','c'),
        b=('c','d'),
        e=(),
        f=('c','e'),
        g=('h','f'),
        i=('f',)
    )
    print dep(d)
