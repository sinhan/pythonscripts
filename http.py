import requests

url = 'http://httpbin.org/post'

files={'file' : ('mycsv.csv', open('mycsv.csv', 'rb'))}

r = requests.post(url, files=files)

print r
