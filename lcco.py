from collections import namedtuple
import string
import sys

import rdflib
import skos

LCCO_URI = 'http://inkdroid.org/lcco/'
LCC = namedtuple('LCC', ['cls', 'subcls', 'topic'])

# create RDF graph
graph = rdflib.Graph()
with open('data/lcco.rdf') as skosfile:
    graph.parse('data/lcco.rdf')

# create SKOS representation
loader = skos.RDFLoader(graph)

# Takes cls, subcls, topic returns next one up
def parse_lcc(lcc):
    cls = lcc[0]
    if len(lcc) > 1:
        subcls = lcc[1] if lcc[1] in string.uppercase else None
        topic = lcc[2:] if subcls else lcc[1:]
    else:
        subcls = None
        topic = None
    return LCC(cls, subcls, topic)


def get_closest(lcc):
    # FIRST SELECT CLOSEST
    if loader.get(LCCO_URI + lcc, False):
        closest = lcc

    parsed = parse_lcc(lcc)
    if parsed.cls != 'E' and parsed.cls != 'F':
        cur_uri = LCCO_URI + parsed.cls
    else:
        cur_uri = LCCO_URI + 'E-F'
    next_uri = [narrow for narrow, obj in loader[cur_uri].narrower.iteritems()
                    if in_range(lcc,str(obj.notation))]

    while next_uri:
        cur_uri = next_uri[0]
        next_uri = [narrow for narrow, obj in loader[cur_uri].narrower.iteritems() 
                        if in_range(lcc,str(obj.notation))]
    
    return str(loader[cur_uri].notation)

def get_next(lcc):
    closest = get_closest(lcc)
    closest_uri = LCCO_URI + closest
    if loader[closest_uri].broader:
        return str(loader[closest_uri].broader.values()[0].notation)
    else:
        return ''

def in_range(lcc, candidate):
    lcc = parse_lcc(lcc)
    candidate = parse_lcc(candidate)
    if lcc.cls != candidate.cls:
        if (lcc.cls == 'E' or lcc.cls =='F') and candidate.cls == 'E-F':
            return True
        return False
    elif candidate.subcls and lcc.subcls != candidate.subcls:
        return False
    elif candidate.topic:
        if not lcc.topic:
            return False
        if lcc.topic == candidate.topic:
            return True
        elif '-' in candidate.topic and '-' not in lcc.topic:
            topic_range = candidate.topic.split('-')
            if '.' in topic_range[0]:
                topic_range[0] = topic_range[0].split('.')[0]
            if '.' in topic_range[1]:
                topic_range[1] = topic_range[1].split('.')[0]
            return int(topic_range[0]) <= int(lcc.topic) <= int(topic_range[1])
        elif '-' in candidate.topic and '-' in lcc.topic:
            lcc_range = lcc.topic.split('-')
            topic_range = candidate.topic.split('-')
            if '.' in topic_range[0]:
                topic_range[0] = topic_range[0].split('.')[0]
            if '.' in topic_range[1]:
                topic_range[1] = topic_range[1].split('.')[0]
            if '.' in lcc_range[0]:
                lcc_range[0] = lcc_range[0].split('.')[0]
            if '.' in lcc_range[1]:
                lcc_range[1] = lcc_range[1].split('.')[0]
            return int(topic_range[0]) <= int(lcc_range[0])\
                    and int(lcc_range[1]) <= int(topic_range[1])
            
        else:
            return False
    else:
        return True

if __name__ == '__main__':
    assert in_range("LB", "L") == True
    assert in_range("L", "LB") == False

    assert get_closest("LB1138") == "LB1101-1139"
    assert get_next("LB1138") == "LB5-3640"

    closest = get_closest(sys.argv[-1])
    if closest == sys.argv[-1]:
        print get_next(closest)
    else:
        print closest

