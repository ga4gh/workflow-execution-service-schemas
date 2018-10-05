#!/usr/bin/env bash

set -e
set -v

if [ "$TRAVIS_BRANCH" == "master" ]; then
    cp docs/html5/index.html docs/
elif [ "$TRAVIS_BRANCH" !=  "gh-pages" ]; then
  branch=$(echo "$TRAVIS_BRANCH" | awk '{print tolower($0)}')
  branchpath="preview-docs/$branch"
  mkdir -p "$branchpath/docs"
  cp docs/html5/index.html "$branchpath/docs/"
fi

