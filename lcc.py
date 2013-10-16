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
from collections import defaultdict
from glob import iglob as glob
import io
import json
import os.path
from time import sleep
import urllib
import xml.etree.ElementTree as ET

def get_lccns(directory):
    # build list of LCCNS from directory
    lccns = dict()

    for json_file in glob(directory + '/*/*.json'):
        dirname = os.path.dirname(json_file)

        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        for record in data['records'].itervalues():
            lccn = record.get("lccns")
            if lccn:
                assert len(lccn) == 1
                lccns[dirname] = lccn[0]
            else:
                marc = parse_marc(record['marc-xml'].encode('utf-8'))
                marc_lccn = get_lccn_from_marc(marc)
                if marc_lccn:
                    lccns[dirname] = marc_lccn


    return lccns

def get_lccs(lccns):
    lccs = dict()
    
    for path, lccn in lccns.iteritems():
        loc_marc_path = os.path.join(path, "loc.marc.xml")
        print loc_marc_path
        if not os.path.exists(loc_marc_path):
            get_loc_marc(lccn, loc_marc_path)
        
        
        if os.path.exists(loc_marc_path):
            try:
                xml = ET.parse(loc_marc_path).getroot()
                lccs[path] = get_lcc_from_marc(xml)
            #except UnicodeDecodeError:
            #    pass
            except ET.ParseError:
                pass

    return lccs

def parse_marc(raw):
    # lazy workaround
    # raw = raw.replace(' xmlns', ' xmlnamespace')
    # ET.register_namespace('', 'http://www.loc.gov/MARC21/slim')
    return ET.fromstring(raw)

def get_marc_value(xml, tag, code):
    xpath = "{marc}datafield[@tag='{tag}']/{marc}subfield[@code='{code}']".format(
                tag=tag, code=code, marc="{http://www.loc.gov/MARC21/slim}")
    results = xml.findall(xpath)
    return results[0].text if results else None

def get_lccn_from_marc(xml):
    lccn = get_marc_value(xml, '010', 'a')
    return lccn



def get_lcc_from_marc(xml):
    # MARC tag 050a/b or 991h/i
    lcc = list()
    val = get_marc_value(xml, '050', 'a')
    if val:
        lcc.append(val)
    
    val = get_marc_value(xml, '050', 'b')
    if val:
        lcc[-1] += val

    val = get_marc_value(xml, '991', 'h')
    if val:
        lcc.append(val)

    val = get_marc_value(xml, '991', 'i')
    if val:
        lcc[-1] += val

    return ";".join(lcc)

def get_loc_marc(lccn, local_copy):
    sleep(5)
    url = 'http://lccn.loc.gov/{lccn}/marcxml'.format(lccn=lccn)
    print url
    raw = urllib.urlopen(url)
    if raw.getcode() < 400:
        if raw.info().get('Content-Type', '') == 'application/xml':
            print "writing contents to", local_copy
            with open(local_copy, 'w', encoding='utf-8') as f:
                text = raw.read().decode('utf-8')
                f.write(text)
        else:
            print "url not xml", url
    else:
        print "could not retrieve", url

if __name__ == '__main__':
    import argparse
    import csv

    directory = 'data/htrc'
    outfile = 'htrc1315.csv'
    lccns = get_lccns(directory)
    lccs = get_lccs(lccns)

    total = 0
    no_lccn = 0
    no_lcc = 0
    with open(outfile, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for json_file in glob(directory + '/*/*.json'):
            dirname = os.path.dirname(json_file)
            htrc_id = os.path.split(dirname)[-1]
            writer.writerow(
                [htrc_id, lccns.get(dirname,''),lccs.get(dirname,'')])
            total += 1
            if not lccns.get(dirname):
                no_lccn += 1
            if not lccs.get(dirname):
                no_lcc += 1


    print total, no_lccn, no_lcc

