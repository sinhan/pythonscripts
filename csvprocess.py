import csv
from urllib import urlopen, urlretrieve
#from operator import itemgetter

csvurl='http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

urlretrieve(csvurl, "mycsv.csv")



with open("mycsv.csv", 'rU') as f:
  f_csv=csv.reader(f, delimiter=',',dialect=csv.excel_tab)
  header=next(f_csv)
  for rows in f_csv:
    if rows: print rows[0]
    #print rows if rows

  t = [row for i,row in enumerate(f_csv) if i > 0]
  #t_new = sorted(t, key=itemgetter(3), reverse=True)
  t_new = sorted(t, key=lambda row: row[3], reverse=True)
  for line in t_new:
      print line   

