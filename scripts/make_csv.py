import csv
import json

htrc1314 = []
htrc86 = []
htrc6=["uc2.ark+=13960=t5w66bs1h",
"uc2.ark+=13960=t6057f659",
"uc2.ark+=13960=t74t6gs0m",
"uc2.ark+=13960=t0ht2h954",
"uc2.ark+=13960=t05x26n0d",
"uc2.ark+=13960=t5p84550z"]

with open('htrc86.json') as jsonfile:
    data = json.load(jsonfile)
    volumes = data.keys()

with open('../data/csv/htrc_lcco.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        htrc1314.append(row['id'])
        if row['id'] in volumes:
            htrc86.append(row['id'])

print len(htrc1314), len(htrc86), len(htrc6)

with open('../data/htrc/1314.txt', 'w') as txtfile:
    txtfile.writelines(htrc1314)
with open('../data/htrc/86.txt', 'w') as txtfile:
    txtfile.writelines(htrc86)
with open('../data/htrc/6.txt', 'w') as txtfile:
    txtfile.writelines(htrc6)
