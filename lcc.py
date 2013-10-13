"""
lcc.py
Takes a folder of HTRC metadata files in JSON format and parses the MARC fields
to find the LCCN. It then requests the record from the http://lccn.loc.gov/ and
parses the LCC classification. The LCC classification is finally looked up in
lcco.rdf and the list of unique names is sorted and printed.

LCC to Dewey Decimal Classification
http://www.questionpoint.org/crs/html/help/it/ask/ask_map_lcctoddc.html

Converting MARC to MODS via XSLT: Converted from MARCXML to MODS version 3.4
using MARC21slim2MODS3-4.xsl (Revision 1.85 2013/03/07)
"""

from codecs import open
from glob import iglob as glob
import io
import json
import os.path
from time import sleep
import urllib
import xml.etree.ElementTree as ET

def get_lccns(directory):
    # build list of LCCNS from directory
    lccns = set()

    for json_file in glob(directory + '/*/*.json'):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        for record in data['records'].itervalues():
            lccn = record.get("lccns")
            if lccn:
                assert len(lccn) == 1
                lccns.add(lccn[0])
            
            marc = parse_marc(record['marc-xml'].encode('utf-8'))
            marc_lccn = get_lccn_from_marc(marc)
            if marc_lccn:
                lccns.add(marc_lccn)

    return lccns

def get_lccs(lccns):
    lccs = set()
    lccns = list(lccns)

    for lccn in lccns[:5]:
        get_lcc(lccn)

    return lccs

def parse_marc(raw):
    # lazy workaround
    raw = raw.replace(' xmlns', ' xmlnamespace')
    ET.register_namespace('', 'http://www.loc.gov/MARC21/slim')
    return ET.fromstring(raw)

def get_marc_value(xml, tag, code):
    xpath = "./record/datafield[@tag='{tag}']/subfield[@code='{code}']".format(
                tag=tag, code=code)
    results = xml.findall(xpath)
    return results[0].text if results else None

def get_lccn_from_marc(xml):
    lccn = get_marc_value(xml, '010', 'a')
    return lccn

def get_lcc(lccn):
    sleep(5)
    url = 'http://lccn.loc.gov/{lccn}/marcxml'.format(lccn=lccn)
    print url
    raw = urllib.urlopen(url)
    if raw.getcode() < 400:
        if raw.info.get('Content-Type', '') == 'application/xml':
            marc = ET.parse(raw).getroot()
            return get_lcc_from_marc(marc)
        else:
            print "url not xml", url
    else:
        print "could not retrieve", url
        return None



def get_lcc_from_marc(xml):
    # MARC tag 050a/b or 991h/i
    lcc = get_marc_value(xml, '050', 'a')
    if lcc is None:
        lcc = get_marc_value(xml, '050', 'b')
    if lcc is None:
        lcc = get_marc_value(xml, '991', 'h')
    if lcc is None:
        lcc = get_marc_value(xml, '991', 'i')

    return lcc

if __name__ == '__main__':
    import argparse

    print get_lccs(get_lccns('data/htrc'))

