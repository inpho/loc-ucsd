"""
Script to enhance the htrc_lcco mapping with metadata from the HTRC Solr index.
"""

import csv
import json
from time import sleep
from urllib2 import urlopen

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
                    solr ="http://chinkapin.pti.indiana.edu:9994/solr/meta/select/?q=id:%s" % row['id']
                    solr += "&wt=json" ## retrieve JSON results
                    data = json.load(urlopen(solr))
                    title = data['response']['docs'][0]['title'][0]
                    sleep(2) ## IMPORTANT: THROTTLE REQUESTS
                except:
                    print row['id'], "SOLR error"
    
                # write CSV row 
                try:
                    url_id = row['id'].replace('+=','/').replace('=','/') #used
                    below
                    writer.writerow({
                        'name' : row['id'],
                        'x' : float(row['match_x']),
                        'y' : 360 - float(row['match_y']),
                        'title' : title,
                        'url' : "http://hdl.handle.net/2027/%s" % url_id,
                        'group' : 0,
                        '_size' : 3.0,
                        'color' : 'Grey', 
                        'id' : i
                        })
                except:
                    print row['id'], "writer error"

                i+= 1 # iterate the magic variable
