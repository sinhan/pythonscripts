#!/usr/bin/python

from urllib.request import urlopen
import json
import pprint

url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'

response=urlopen(url)

mystring=response.read().decode('utf-8')

json_obj=json.loads(string)

pprint(json_obj)
