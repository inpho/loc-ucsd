import csv
import json

with open('htrc86.json') as jsonfile:
    data = json.load(jsonfile)
    volumes = data.keys()


vol6=["uc2.ark+=13960=t5w66bs1h",
"uc2.ark+=13960=t6057f659",
"uc2.ark+=13960=t74t6gs0m",
"uc2.ark+=13960=t0ht2h954",
"uc2.ark+=13960=t05x26n0d",
"uc2.ark+=13960=t5p84550z"]

rows86 = []
rows6 = []

with open('../www/htrc_coords_new.csv', 'rb') as origfile:
    with open('htrc_coords_new6.csv', 'wb') as newfile:
        reader = csv.DictReader(origfile)
        writer = csv.DictWriter(newfile, ['id', 'x', 'y', 'title','url','htrc86','htrc6'])
        for row in reader:
            row.update({'htrc86' : str(row['id'] in volumes).lower()})
            row.update({'htrc6' : str(row['id'] in vol6).lower()})
            if row['htrc86'] == 'true':
                if row['htrc6'] == 'true':
                    rows6.append(row)
                else:
                    rows86.append(row)
            else:
                writer.writerow(row)

        for row in rows86:
            writer.writerow(row)
        for row in rows6:
            writer.writerow(row)
