import json
from urllib import urlopen, urlretrieve



url1="http://offers-creditkarma.rhcloud.com/offers/auto-loan"
url2="http://offers-creditkarma.rhcloud.com/offers/credit-card"
url3="http://offers-creditkarma.rhcloud.com/offers/personal-loan"

urlretrieve(url1, "myjson.json")
with open('myjson.json', 'rU') as data_file:
    data = json.load(data_file)
print data



#myoffers={"Autoloan" : url1, "CreditCard" : url2 , "PersonalLoan" : url3}
myoffers={"Autoloan" : url1}

for k,v in myoffers.items():
    print "---- %s ------" %(k)
    myurl=urlopen(v).read().decode('utf-8')
    jsonobj=json.loads(myurl)
    for lines in jsonobj:
        for a,b in lines.items():
            print "**"
            for m,n in b.items():
                print m, n 
