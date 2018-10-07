#!/usr/bin/env node
'use strict';
var path = require('path');

require('shelljs/global');

set('-e');
set('-v');

var branch = process.env.TRAVIS_BRANCH && process.env.TRAVIS_BRANCH.toLowerCase();
if (branch && branch == 'master') {
    cp('-R', 'web_deploy/*', './');
} else if (branch && branch !== 'gh-pages') {
  var branchPath = path.join('preview', branch, '/');
  mkdir('-p', branchPath);
  cp('-R', 'web_deploy/*', branchPath);
}
