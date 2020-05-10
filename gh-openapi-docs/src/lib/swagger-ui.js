#!/usr/bin/env node
'use strict';
import shell from 'shelljs';
import path from 'path';
import config from './config';
import Log from './log';

const log = new Log();

var SWAGGER_UI_DIST = require("swagger-ui-dist").getAbsoluteFSPath();
var SHARED_UI_PATH = path.join(config.root, 'shared', config.uiRoot);
var SWAGGER_JSON_PATH = path.join(config.branchPath, 'openapi.json');

const getAssets = () => {
    shell.rm('-rf', SHARED_UI_PATH);
    shell.mkdir('-p', path.join(config.root, 'shared'));
    shell.cp('-R', SWAGGER_UI_DIST, SHARED_UI_PATH);
};

const setupUI = () => {
    getAssets()
    var uiPath = path.join(config.branchPath, config.uiRoot);
    shell.mkdir('-p', uiPath);
    log.log(`Copying Swagger UI index to '${uiPath}'`);
    shell.cp(path.join(SHARED_UI_PATH, 'index.html'), `${uiPath}/`);
    log.preview({
        'title': 'Swagger UI folder contents',
        'text': shell.ls(uiPath).stdout
    });
    log.log(`Updating API spec path for '${path.join(uiPath, 'index.html')}'`);
    shell.sed(
        '-i',
        /\.\//,
        `${path.relative(uiPath, SHARED_UI_PATH)}/`,
        [path.join(uiPath, 'index.html')]
    );
    var swagger_spec = require(`${SWAGGER_JSON_PATH}`);
    shell.sed(
        '-i',
        'url: "https://petstore.swagger.io/v2/swagger.json"',
        `spec: ${JSON.stringify(swagger_spec)}`,
        [path.join(uiPath, 'index.html')]
    );
};

// setupUI()
export { getAssets, setupUI };
