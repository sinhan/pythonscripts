import tarfile
import os
import shutil

with tarfile.open("myarchive.gz" , "w:gz") as tar:
    for name in ["test123", "classes.py"]:
       tar.add(name)
    
tar.close()

tar = tarfile.open("myarchive.gz", "r:gz")
for tarinfo in tar:
   print tarinfo.name, tarinfo.size ,
   if tarinfo.isreg():
      print "regular file"
   elif  tarinfo.isdir():
      print " directory"
   else:
      print " fishy"
names=tar.getmembers()
print names
tar.close()

#os.mkdir("myarchivetest")
#os.chdir("myarchivetest")

tar=tarfile.open("myarchive.gz")
tar.extractall("new/mytestsarchive")
tar.close()
