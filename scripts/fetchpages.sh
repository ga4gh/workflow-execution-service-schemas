#!/usr/bin/env bash

set -e
set -v

rm -rf .ghpages-tmp
mkdir -p .ghpages-tmp
cd .ghpages-tmp
git clone --depth=1 --branch=gh-pages $REPO_URL .
cp -Rn preview ../preview/
cd ..


