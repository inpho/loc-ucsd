import csv

lcco = dict()
ucsd = dict()

with open('htrc_lcco.csv', 'rb') as htrc_lcco_file:
    reader = csv.DictReader(htrc_lcco_file, delimiter=",", quotechar="\"")
    for row in reader:
        lcco[row['id']] = row['matched_class'] + row['matched_subclass'] + row['matched_lowtopic']

with open('lcco_ucsd.csv', 'rb') as lcco_ucsd_file:
    reader = csv.DictReader(lcco_ucsd_file, delimiter=",", quotechar="\"")
    for row in reader:
        ucsd[row['LoC']] = row['subd_id']

errors = 0
for lcco in lcco.itervalues():
    try:
        print ucsd[lcco]
    except:
        errors += 1

print errors, "journals not found"
