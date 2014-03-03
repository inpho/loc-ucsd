from argparse import ArgumentParser, FileType
from codecs import open
from collections import defaultdict
import json
from time import sleep
import xml.etree.ElementTree as ET

import htrc
import lcc

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

    volumes = [line.strip() for line in args.volume_file]
    for htrc, lccn in get_lccns(volumes).iteritems():
        print htrc, lccn
