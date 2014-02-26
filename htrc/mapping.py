import htrc
"""
The stuff in lcc is all relative to local file paths that may or may not exist
anymore. Probably not. Defintiely not.

Still, the code is correct for doing the actual parsing once you get the file
data. Some of it is path dependent, some is data dependent, edit lcc to make it
data dependent, rather than path dependent.
"""
import lcc

#open up 'data/htrc/1315.csv', '86.csv', '6.csv', etc.

#pseudo-code
def find_ucsd_mappings(id):
    metadata = htrc.metadata(id)
    # do some stuff to find the LCCN - look at lcc.py
    lccn = lcc.get_lccn(metadata) # demo data

    # look up the LCC using lcco.py
    lcc.get_lccs(lccns)

    # look up the UCSD mapping using 'data/csv/lcco_ucsd.csv'
    return ucsd[lcc]
