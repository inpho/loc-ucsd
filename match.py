"""
Script to match UCSD Subdisciplines to LoC Subject Headings.
Uses the data files downloaded by fetch-data.sh.

Requires RDFLib
"""
import csv
from urllib import quote_plus
from urllib2 import HTTPError, urlopen, URLError

ucsd_data = 'data/UCSDmap.net'
loc_data = 'data/subjects-skos.nt'

# LoC Known-label retrieval: http://id.loc.gov/techcenter/searching.html
loc_label_uri = 'http://id.loc.gov/authorities/subjects/label/'
loc_subject_uri = 'http://id.loc.gov/authorities/subjects/'

def get_subdisciplines(filename):
    vertices = None
    nodes = dict()

    with open(filename) as csvfile:
        netreader = csv.reader(csvfile, delimiter=' ', quotechar='"')

        for row in netreader:
            # process number of verticies
            if not vertices and row[0] == '*vertices':
                vertices = row[1]
                continue

            # terminate execution when edges reached
            if row[0] == '*edges':
                break

            # process node
            if vertices:
                nodes[row[0]] = row[1]

    return nodes

def match(label):
    try:
        response = urlopen(loc_label_uri + label)
        url = response.geturl()
        subject = url.replace(loc_subject_uri, '').replace('.html', '')
        return subject

    except (HTTPError, URLError):
        return None
    

if __name__ == '__main__':
    for id, name in get_subdisciplines(ucsd_data).iteritems():
        print id, match(quote_plus(name)) 

