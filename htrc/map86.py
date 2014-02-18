import csv
import json

with open('htrc86.json') as jsonfile:
    data = json.load(jsonfile)
    volumes = data.keys()

count =0 
with open('../www/htrc_coords.csv', 'rb') as origfile:
    with open('htrc_coords_new.csv', 'wb') as newfile:
        reader = csv.DictReader(origfile)
        writer = csv.DictWriter(newfile, ['id', 'x', 'y', 'title', 'url','htrc86'])
        for row in reader:
            row.update({'htrc86' : str(row['id'] in volumes).lower()})
            if row['id'] in volumes:
                count += 1
            writer.writerow(row)

print count
