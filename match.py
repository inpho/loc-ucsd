"""
Script to match UCSD Subdisciplines to LoC Subject Headings.
Uses the data files downloaded by fetch-data.sh.

Requires RDFLib
"""
import csv
from rdflib.graph import Graph
from rdflib.term import URIRef, Literal

ucsd_data = 'data/UCSDmap.net'
loc_data = 'data/subjects-skos.nt'
loc_data = 'data/skos.nt'
skos_prefLabel = URIRef("http://www.w3.org/2004/02/skos/core#prefLabel")
skos_altLabel = URIRef("http://www.w3.org/2004/02/skos/core#altLabel")

def get_subdiscipline_names(filename):
    with open(filename) as csvfile:
        vertices = None
        nodes = []

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
                print row
                nodes.append(row[1])

    return nodes

def get_loc_graph(filename):
    g = Graph()
    g.parse(filename, format="nt")
    return g

def match(label, g):
    m = g.subjects(skos_prefLabel, Literal(label))
    if not m:
        m = g.subjects(skos_altLabel, Literal(label))
    return m
    

if __name__ == '__main__':
    for name in get_subdiscipline_names(ucsd_data):
        print name

