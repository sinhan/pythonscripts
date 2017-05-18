deps = {"x":
    {"y":{},
     "z":{"a":{}}
    }}

def makeTree(files):
	"""Pass in a list of files for which dependency info
	should be generated."""

	deps = {}
	cur_files = [(fname,deps) for fname in files]
	all_deps = {}
	while cur_files:
		cur_file, cur_deps = cur_files.pop()
		if cur_file in all_deps:
			cur_deps[cur_file] = all_deps[cur_file]
			continue
		new_deps = {}
		# getDeps returns the dependencies needed by cur_file.
		for dep in getDeps(cur_file):
			cur_files.append((dep,new_deps))
		cur_deps[cur_file] = new_deps
		all_deps[cur_file] = new_deps
	return deps
