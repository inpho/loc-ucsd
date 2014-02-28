import csv
import json

htrc1314 = []
htrc86 = []
htrc6 = []
volumes6=["uc2.ark+=13960=t5w66bs1h",
"uc2.ark+=13960=t6057f659",
"uc2.ark+=13960=t74t6gs0m",
"uc2.ark+=13960=t0ht2h954",
"uc2.ark+=13960=t05x26n0d",
"uc2.ark+=13960=t5p84550z"]

with open('htrc86.json') as jsonfile:
    data = json.load(jsonfile)
    volumes86 = data.keys()

with open('../data/csv/htrc_lcco.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['id'] in volumes6:
            htrc6.append({'id' : row['id'], 
                          'lccn' : row['id2'],
                          'collection' : 'htrc6'})
        elif row['id'] in volumes86:
            htrc86.append({'id' : row['id'], 
                           'lccn' : row['id2'],
                           'collection' : 'htrc86'})
        else:
            htrc1314.append({'id' : row['id'], 
                             'lccn' : row['id2'],
                             'collection': 'htrc1314'})

print len(htrc1314), len(htrc86), len(htrc6)

with open('../data/htrc/all.csv', 'w') as newfile:
    writer = csv.DictWriter(newfile, ['id', 'lccn'], extrasaction='ignore')
    for row in htrc6:
        writer.writerow(row)
    for row in htrc86:
        writer.writerow(row)

