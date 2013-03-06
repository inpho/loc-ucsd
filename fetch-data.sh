#!/bin/sh
# Script to retrieve datasets for loc-ucsd mapping.
# Will not redownload information if no update.

# LoC Data
mkdir data
wget -NP data http://id.loc.gov/static/data/authoritiessubjects.nt.skos.zip
unzip -fo data/authoritiessubjects.nt.skos.zip -d data

# UCSD Data
wget -NP data http://sci.cns.iu.edu/ucsdmap/data/UCSDmap.net 
