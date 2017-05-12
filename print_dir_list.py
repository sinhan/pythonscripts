import os
def list_my_dir(d):
   for i in os.listdir(d):
      fullpath=os.path.join(d,i)
      print fullpath
      if os.path.isdir(fullpath):
         list_my_dir(fullpath)

list_my_dir("projects")

print "---" * 5

script_location = os.path.dirname(os.path.abspath(__file__))
script_location = "projects"

for dirpath, dirs, files in os.walk(script_location):
  for f in files:
    print(os.path.join(dirpath,f))

