from argparse import ArgumentParser, FileType
from codecs import open
from collections import defaultdict
import json
from time import sleep
import xml.etree.ElementTree as ET

import htrc
import lcc

def test():
    id = "uc2.ark+=13960=t0ht2h954"
    data = htrc.metadata(id)
    print data['fullrecord']
    marc = lcc.parse_marc(data['fullrecord'])
    print marc
    print lcc.get_marc_value(marc, '245', 'a')
    assert lcc.get_lccn_from_marc(marc) == "10006734"

def get_lccns(volumes):
    lccn = dict()
    for volume in volumes:
        metadata = htrc.metadata(volume)
        lccn[volume] = lcc.get_lccn(metadata)

    return lccn

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('volume_file', type=FileType('r'))
    args = parser.parse_args()

    test()
    """
    volumes = [line.strip() for line in args.volume_file]
    for htrc, lccn in get_lccns(volumes).iteritems():
        print htrc, lccn
    """
