'use strict';
import shell from 'shelljs';
import config from './config';
import Log from './log';
import fs from 'fs';


const log = new Log();

const fetchPages = () => {
    shell.rm('-rf', '.ghpages-tmp');
    shell.mkdir('-p', '.ghpages-tmp');
    var startDir = shell.pwd();
    shell.cd('.ghpages-tmp');
    log.log(`Cloning 'gh-pages' branch into '${shell.pwd().stdout}'`);
    shell.exec(`git clone --depth=1 --branch=gh-pages ${config.repoOrigin} .`);
    shell.cp('-Rn', config.branchPathBase, config.root);
    if (fs.existsSync(config.docsRoot)) {
        shell.cp('-Rn', config.docsRoot, config.root);
        shell.cp('-Rn', 'openapi.*', config.root);
    }
    shell.cd(startDir);
    shell.rm('-rf', '.ghpages-tmp')
};

export { fetchPages };
