var fs = require('fs')
  , request = require('request')
  , cheerio = require('cheerio')
  ;

var getListFromGithub = function(cb) {
  var url = 'https://github.com/search?q=name+extension%3Ajson+path%3Adatapackage.json&type=Code&ref=searchresults';
  request(url, function(err, res, body) {
    if (res.statusCode >= 400) {
      console.log('Status code: ' + res.statusCode);
      return;
    }
    var $ = cheerio.load(body);
    // total number of results
    var total = parseInt($('.selected .counter').text());

    // do the first one to save loading again
    var out = extractReposFromPage($);

    // now go through results pages - 10 results per page
    var pagecount = Math.floor(total/10.0)+1;
    var count = pagecount;
    for(ii=2; ii<=pagecount; ii++) {
      var turl = url + '&p=' + ii;
      console.log(turl);
      request(turl, function(err, res, body) {
        count --;
        var $ = cheerio.load(body);
        var tmp = extractReposFromPage($);
        out = out.concat(tmp);
        if (count === 1) {
          cb(null, out);
        }
      });
    }
  });
};

function extractReposFromPage($) {
  var out = [];
  $('#code_search_results .title a:first-child').each(function(idx, el) { 
    var userPlusRepo = $(el).text();
    var url = 'https://github.com/' + userPlusRepo;
    out.push(url);
  });
  return out;
}

getListFromGithub(function(err, dpkgs) {
  if (err) {
    console.error(err);
  } else {
    dpkgs.sort();
    var out = dpkgs.join('\n');
    fs.writeFileSync('github-list.txt', out);
  }
});

