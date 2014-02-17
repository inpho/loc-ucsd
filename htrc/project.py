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

## process the json generated from the map file
with open("mapOfScienceData.json") as mapdata:
    data = json.load(mapdata)
    for subd in data['nodes']:
        print subd
        diffs[subd['id']] = Pair(subd['x'], subd['y'])

## process the CSV generated from the LOC data analysis.
with open("subd_coords.csv", 'rb') as newdata:
    reader = csv.DictReader(newdata, delimiter=",",quotechar="\"")
    for row in reader:
        a = diffs[int(row['subd_id'])]
        b = Pair(row['x'], row['y'])
        ## calculate difference
        diffs[int(row['subd_id'])] -= Pair(row['x'], row['y'])

        ## some nice logging
        print row['subd_id'], a, b, a - b

## average diffs
print "average diff"
print reduce(lambda x,y: x+y, diffs.values()) / Pair(len(diffs), len(diffs))
