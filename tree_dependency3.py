class Node:
   def __init__(self, name):
          self.name = name
          self.edges = []
   def addEdge(self, node):
       self.edges.append(node)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.addEdge(b)    # a depends on b
a.addEdge(d)    # a depends on d
b.addEdge(c)    # b depends on c
b.addEdge(e)    # b depends on e
c.addEdge(d)    # c depends on d
c.addEdge(e)    # c depends on e

def dep_resolve(node, resolved, seen):
   print node.name
   seen.append(node)
   for edge in node.edges:
          if edge not in resolved:
                 if edge in seen:
                        raise Exception('Circular reference detected: %s -&gt; %s' % (node.name, edge.name))
                 dep_resolve(edge, resolved, seen)
   resolved.append(node)

resolved = []
dep_resolve(a, resolved, [])
for node in resolved:
   print node.name,

