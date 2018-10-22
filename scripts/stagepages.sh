#!/usr/bin/env bash

set -e
set -v

if [ "$TRAVIS_PULL_REQUEST" != false ]; then
  branch="pull-$TRAVIS_PULL_REQUEST"
else
  branch=$(echo "$TRAVIS_BRANCH" | awk '{print tolower($0)}')
fi


if [ "$TRAVIS_BRANCH" == "master" ] || [ "$TRAVIS_BRANCH" == "develop" ]; then
    cp docs/html5/index.html docs/
    cp openapi/workflow_execution_service.swagger.yaml ./swagger.yaml
    cp -R web_deploy/* .
elif [ "$TRAVIS_BRANCH" != "gh-pages" ]; then
  branchpath="preview/$branch"
  mkdir -p "$branchpath/docs"
  cp docs/html5/index.html "$branchpath/docs/"
  cp openapi/workflow_execution_service.swagger.yaml "$branchpath/swagger.yaml"
  cp -R web_deploy/* "$branchpath/"
fi

