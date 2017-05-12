import csv
from operator import itemgetter

with open("mycsv.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    t = [row for i,row in enumerate(reader) if i > 0]

t_new = sorted(t, key=itemgetter(5), reverse=True)
for line in t_new:
    print line
