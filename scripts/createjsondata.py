import csv
import json
from collections import namedtuple

## Just for convenience, a  nice pair object
class Pair(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "(%2f, %2f)" % (self.x, self.y)

    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Pair(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Pair(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Pair(self.x / other.x, self.y / other.y)

## initialize a dictionary to store the differences in
diffs = dict()
links = dict()

## process the json generated from the map file
with open("mapOfScienceData.json") as mapdata:
    data = json.load(mapdata)
    links = data['links']
    for subd in data['nodes']:
        diffs[subd['id']] = subd

## process the CSV generated from the LOC data analysis.
with open("../data/csv/subd_coords.csv", 'rb') as newdata:
    reader = csv.DictReader(newdata, delimiter=",",quotechar="\"")
    for row in reader:
        diffs[int(row['subd_id'])]['x'] = float(row['x'])
        diffs[int(row['subd_id'])]['y'] = float(row['y'])

print json.dumps({'nodes' : diffs.values(), 'links' : links})
