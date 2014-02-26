import csv

with open('htrc_lcco.csv', 'rb') as htrc_lcco_file:
    reader = csv.DictReader(htrc_lcco_file, delimiter=",", quotechar="\"")
    with open('htrc_coords.csv', 'wb') as writefile:
        writer = csv.writer(writefile, delimiter=',')
        writer.writerow(['id','match_x','match_y'])
        for row in reader:
            if row['match_x'] != '-' and row['match_y'] != '-':
                writer.writerow([row['id'], row['match_x'], row['match_y']])
