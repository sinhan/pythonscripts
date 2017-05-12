#!/usr/bin/python

from urllib import urlopen, urlretrieve
import json
import pprint
import requests
import csv
import yaml

url = 'https://www.quandl.com/api/v1/datasets/FRED/GDP.json'

response=urlopen(url)
response1=urlopen(url)
r=requests.get(url)
#print r.json()['source_name']
print  r.json()

urlretrieve(url, "test.txt")


mystring=response.read().decode('utf-8')

json_obj=json.loads(mystring)
#print(json_obj['source_name'])
with open('data.txt', 'w') as outfile:
    json.dump(json_obj, outfile)


#with open('data.txt') as data_file:
#    data = json.load(data_file)
#print data
data = json.load(open('data.txt'))
#print(data['source_name'])
#pprint(data)

csvurl='http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

with requests.Session() as s:
   download = s.get(csvurl)

   decoded_content = download.content.decode('utf-8')
   cr = csv.reader(decoded_content.splitlines(), delimiter=',')
   my_list = list(cr)
   for row in my_list:
      print(row)
      break

urlretrieve(csvurl, "mycsv.csv")

with open('mycsv.csv', 'rU') as f:
    reader = csv.reader(f, delimiter=',', dialect=csv.excel_tab)
#    your_list = list(reader)
    for row in reader:
      print(row)
      break

#print your_list

resp=requests.head("http://www.google.com")
for x in resp.headers:
   print x, ":" ,  resp.headers[x]

with open('tree.yaml', 'r') as f:
    doc = yaml.load(f)
txt = doc["treeroot"]["branch1"]
print txt

