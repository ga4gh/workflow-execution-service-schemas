// #!/usr/bin/env node
'use strict';
import shell from "shelljs";
import path from 'path';
import config from './config';
import Log from './log';

const log = new Log();

var OPENAPI_JSON_PATH = path.join(config.branchPath, 'openapi.json');
var OPENAPI_YAML_PATH = path.join(config.branchPath, 'openapi.yaml');

const bundleSpec = async () => {
    log.preview({
        'title': 'Branch folder',
        'text': config.branchPath
    })
    shell.mkdir('-p', config.branchPath);
    var specDir = path.join(config.root, 'spec');
    shell.mkdir('-p', specDir);

    var specPath = path.join(config.root, config.apiSpecPath);

    log.preview({
        'title': 'Spec location',
        'text': specPath
    })

    shell.cp(specPath, path.join(config.root, 'spec/openapi.yaml'));

    log.log("\nBundling API spec...");
    log.preview({
        'title': 'Storing to',
        'text': OPENAPI_JSON_PATH
    });
    shell.exec(
        `openapi bundle -f --output ${OPENAPI_JSON_PATH} ${config.apiSpecPath}`
    );
    shell.exec(
        `openapi bundle -f --output ${OPENAPI_YAML_PATH} ${config.apiSpecPath}`
    );
    shell.rm('-rf', specDir);
};

export default bundleSpec;