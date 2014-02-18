var htrc = htrc || {};
htrc.solr = htrc.solr || {};

htrc.solr.host = "http://chinkapin.pti.indiana.edu:9994";

/* htrc.solr.get(id)
 * Performs a query for the given id
 * */
htrc.solr.get = function(id, callback) {
  var url = htrc.solr.host + "/solr/meta/select/?callback=?&q=id:" + id + "&wt=json";
  return $.getJSON(url, callback);
};
