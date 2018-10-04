#!/usr/bin/env node
'use strict';
var path = require('path');

require('shelljs/global');
set('-e');
set('-v');

mkdir('-p', 'spec')
mkdir('-p', 'web_deploy')

cp('openapi/workflow_execution_service.swagger.yaml', 'spec/swagger.yaml');

exec('npm run swagger bundle --        -o web_deploy/swagger.json');
exec('npm run swagger bundle -- --yaml -o web_deploy/swagger.yaml');

var SWAGGER_UI_DIST = path.dirname(require.resolve('swagger-ui'));
rm('-rf', 'web_deploy/swagger-ui/')
cp('-R', SWAGGER_UI_DIST, 'web_deploy/swagger-ui/')
ls('web_deploy/swagger-ui')
sed('-i', 'http://petstore.swagger.io/v2/swagger.json', '../swagger.json', 'web_deploy/swagger-ui/index.html')
