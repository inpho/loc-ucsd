/* htrc.js
 * Helpers for performing solr queries
 * 
 * Requires: 
 * - jQuery 1.11.0
 * - mustache.js
 * */

var htrc = htrc || {};
htrc.solr = htrc.solr || {};

htrc.solr.host = "http://chinkapin.pti.indiana.edu:9994";

/* htrc.solr.get(id)
 * Performs a query for the given id
 * */
htrc.solr.get = function(id, callback) {
  var url = htrc.solr.host + "/solr/meta/select/?q=id:" + id + "&wt=json";
  $.ajax({
    dataType: 'jsonp',
    url: url,
    success: callback,
    'jsonp' : 'json.wrf'
  });
  return true; 
};


htrc.popover = function(elt) {
  htrc.solr.get($(elt).data('htrc-id'), function (data) {
    data = data.response.docs[0];
    var html = Mustache.to_html($("#template").html(), data);
    $("#container").html(html);
    $(elt).popover({
      content : html,
      title : data['title'][0],
      container : 'body'
    });
  });
};
