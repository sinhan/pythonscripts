import subprocess

def getIPs(file):
   ips = {}
   with open(file) as f:
      for line in f:
         domain = line.strip()
         out = subprocess.check_output(["dig","+noall","+answer", domain])
         ips[domain] = out.split()[4]
   return ips

print getIPs('domains.txt')
