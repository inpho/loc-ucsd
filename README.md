LoC-UCSD Mapping
==================

Attempt to map [Library of Congress Subject Headings](http://id.loc.gov/authorities/subjects.html) onto [UCSD Map of Science Subdisciplines](http://sci.cns.iu.edu/ucsdmap/). All subdiscipline names were first matched along the skos:prefLabel field. Those remaining were then matched against the skos:altLabel field.

If this naive match does not work, I will attempt to look up the journals composing a UCSD subdiscipline and see if I can find any LoC classification for them, and assign the subdiscipline the plurality LoC journal classification.

Datasets
----------
* LoC Subject Headings SKOS/RDF data [NT](http://id.loc.gov/static/data/authoritiessubjects.nt.skos.zip) [rdfxml](http://id.loc.gov/static/data/authoritiessubjects.rdfxml.skos.zip)
* UCSD Data [Network .net file](http://sci.cns.iu.edu/ucsdmap/data/UCSDmap.net) [MS Excel file](http://sci.cns.iu.edu/ucsdmap/data/UCSDmapDataTables.xlsx)
