"""
The stuff in lcc is all relative to local file paths that may or may not exist
anymore. Probably not. Defintiely not.

Still, the code is correct for doing the actual parsing once you get the file
data. Some of it is path dependent, some is data dependent, edit lcc to make it
data dependent, rather than path dependent.
"""

from collections import defaultdict
import htrc
import lcc

#open up 'data/htrc/1315.csv', '86.csv', '6.csv', etc.
with open(volumefile) as f:
    for line in f:
        find_ucsd_mappings(line)

#pseudo-code
def find_ucsd_mappings(id):
    """ Takes an ID and returns a list of ucsd classifications """
    # lookup the metadata for the volume
    metadata = htrc.metadata(id) #this just works

    # do some stuff to find the LCCN - look at lcc.py
    lccn = lcc.get_lccn(metadata) # demo data


def find_classifcation:
    # look up the LCC using lcco.py
    classification = lcc.get_lccs(lccns)

    # using the global dictionary to return the subd_ids
    return ucsd[classification]

def generate_lcc_ucsd_map():
    # look up the UCSD mapping using '../data/csv/lcco_ucsd.csv'
    lcc = defaultdict(list)

    for row in mapfile:
        lcc[row[LoC]].append(row[subd_id])

    return lcc
