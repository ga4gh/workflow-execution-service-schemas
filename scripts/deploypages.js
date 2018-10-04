#!/usr/bin/env node
'use strict';
var path = require('path');

require('shelljs/global');

set('-e');
set('-v');

var branch = process.env.TRAVIS_BRANCH && process.env.TRAVIS_BRANCH.toLowerCase();
if (branch && branch == 'master') {
    cp('-R', 'web_deploy/*', './');
    cp('docs/html5/index.html', 'docs/');
} else if (branch && branch !== 'gh-pages') {
  var branchPath = path.join('preview', branch, '/');
  var branchDocsPath = path.join(branchPath, 'docs', '/');
  mkdir('-p', branchPath);
  mkdir('-p', branchDocsPath);
  cp('-R', 'web_deploy/*', branchPath);
  cp('docs/html5/index.html', branchDocsPath);
}
