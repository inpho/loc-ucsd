LoC-UCSD Mapping
==================

Attempt to map [Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html) onto [UCSD Map of Science Subdisciplines](http://sci.cns.iu.edu/ucsdmap/). 

This is motivated by work with the [HathiTrust Research Center](http://www.hathitrust.org/htrc) (HTRC). Many HTRC volumes contain Library of Congress subject heading metadata, so by mapping a correspondence between the UCSD subdisciplines and LoC subject headings, one can plot HTRC volumes on the Map of Science. Additionally, as the Library of Congress is a central authority for many digital library projects, publishing this correspondence using SKOS will further adoption of the UCSD map.

Methodology
-------------
All subdiscipline names were first matched along the skos:prefLabel field. Those remaining were then matched against the skos:altLabel field. If this naive match does not work, I will attempt to look up the journals composing a UCSD subdiscipline and see if I can find any LoC classification for them, and assign the subdiscipline the plurality LoC journal classification.

A preliminary verification on a matched discipline "Circulation" (under Medical Specialties in UCSD) shows that the best match is ["blood - circulation"](http://id.loc.gov/authorities/subjects/sh85014931.html), but there are 96 subject headings with "circulation" in the title, including ["circulation"](http://id.loc.gov/authorities/subjects/sh2005006524.html) (referring to periodicals). Matches will need to be reviewed, particularly in cases where multiple matches may exist. 

Execution
-----------
1. Run `fetch-data.sh` to retrieve the datasets necessary to run the script.
2. Run `python match.py` to match based on skos:prefLabel, using the [known-label retrieval API](http://id.loc.gov/techcenter/searching.html). Pipe output to a file, if so desired: `python match.py > matches.txt`

Datasets
----------
* LoC Subject Headings SKOS/RDF data [NT](http://id.loc.gov/static/data/authoritiessubjects.nt.skos.zip) [rdfxml](http://id.loc.gov/static/data/authoritiessubjects.rdfxml.skos.zip)
* UCSD Data [Network .net file](http://sci.cns.iu.edu/ucsdmap/data/UCSDmap.net) [MS Excel file](http://sci.cns.iu.edu/ucsdmap/data/UCSDmapDataTables.xlsx)

Output
--------
Final project output will be two alignment files:

1. `loc-ucsd.csv` containing disc_id, disc_name, loc_id, loc_label.
2. `loc-ucsd.skos` containing the skos:exactMatch and skos:closeMatch relations indicating the provenance of automatic vs. manual alignment, respectively. As the [UCSD Map of Science](http://sci.cns.iu.edu/ucsdmap/) does not currently have any semantic data, a URI scheme for subdisciplines must be determined.

