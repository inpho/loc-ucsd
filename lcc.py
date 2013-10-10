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

import json
import xml.etree.ElementTree as ET

def parse_dir(directory):
    # build list of LCCNS from directory
    lccns = set()

    for json_file in glob(directory + '/*.json'):
        with open(json_file) as f:
            metadata = json.load(f)

        for record in data['records'].itervalues():
            lccns.add(record["lccns"])
            marc-lccns = get_lccn_from_marc(record['marc-xml'])

    return lccns

def _parse_marc(raw):
    # lazy workaround
    raw = raw.replace(' xmlns:', ' xmlnamespace:')
    ET.register_namespace('', 'http://www.loc.gov/MARC21/slim')
    root = ET.fromstring(raw)

def get_marc_value(xml, tag, code):
    results = xml.findall(
        "./record/datafield[@tag={tag}]/subfield[@code={code}]" %
        {'name': name, 'tag' : tag})
    return results[0] if results else None

def get_lccn_from_marc(raw):
    # MARC code 010
    pass

def get_lcc_from_marc(raw):
    # MARC tag 050a/b or 991h/i
    pass


if __name__ == '__main__':
    import argparse

    pass
