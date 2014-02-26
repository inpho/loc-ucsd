"""
Script to enhance the htrc_lcco mapping with metadata from the HTRC Solr index.
"""

import csv
import htrc

# open and intialize csv files
with open('htrc_lcco.csv', 'rb') as origfile:
    with open('htrc_coords.csv', 'wb') as newfile:
        reader = csv.DictReader(origfile)
        writer = csv.DictWriter(newfile, ['id', 'x', 'y', 'title', 'url'])

        i = 567 ## WARNING: Magic variable
        for row in reader:
            if row['match_x'] != '-' and row['match_y'] != '-':

                ## retrieve the metadata from Solr 
                try:
                    data = htrc.metadata(row['id'])
                    title = data['response']['docs'][0]['title'][0]
                except:
                    print row['id'], "SOLR error"
    
                # write CSV row 
                try:
                    url_id = row['id'].replace('+=','/').replace('=','/')
                    writer.writerow({
                        'id' : row['id'],
                        'x' : float(row['match_x']),
                        'y' : 360 - float(row['match_y']),
                        'title' : title,
                        'url' : "http://hdl.handle.net/2027/%s" % url_id,
                        })
                except UnicodeEncodeError:
                    print row['id'], "Unicode encoding"

                i+= 1 # iterate the magic variable
