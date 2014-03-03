import json
from time import sleep
from urllib2 import urlopen

def metadata(htrc_id, sleep_time=1):
    """ Queries the HTRC Solr index and returns the metadata.
    Documentation: http://www.hathitrust.org/htrc/solr-api
    """
    # TODO: Parameterize hostname
    solr ="http://chinkapin.pti.indiana.edu:9994/solr/meta/select/?q=id:%s" % htrc_id
    solr += "&wt=json" ## retrieve JSON results
    # TODO: exception handling
    data = json.load(urlopen(solr))
    if sleep:
        sleep(sleep_time) ## JUST TO MAKE SURE WE ARE THROTTLED
    return data['response']['docs'][0]
