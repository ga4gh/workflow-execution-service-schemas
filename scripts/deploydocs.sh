#!/usr/bin/env bash

set -e
set -v

if [ "$TRAVIS_PULL_REQUEST" ]; then
  BRANCH="$TRAVIS_PULL_REQUEST_BRANCH"
else
  BRANCH="$TRAVIS_BRANCH"
fi

if [ "$BRANCH" == "master" ]; then
    cp docs/html5/index.html docs/
    cp openapi/workflow_execution_service.swagger.yaml ./swagger.yaml
elif [ "$BRANCH" !=  "gh-pages" ]; then
  branch=$(echo "$BRANCH" | awk '{print tolower($0)}')
  branchpath="preview/$branch"
  mkdir -p "$branchpath/docs"
  cp docs/html5/index.html "$branchpath/docs/"
  cp openapi/workflow_execution_service.swagger.yaml "$branchpath/swagger.yaml"
fi

