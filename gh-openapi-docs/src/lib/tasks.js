import _ from 'lodash';
import Logger from './log';
import Config from './config';
import { fetchPages } from './gh-pages';
import bundleSpec from './bundle';
import { setupUI } from './redoc-ui';

const runTasks = (opts, di) => {
  let container = {};

  try {
    Object.assign(container, di);
    container.config = container.config || Config;

    container.log = container.log || new Logger();
    const { log } = container;

    console.log(container.config);
    log.obtrusive(`Preparing docs for API spec at '${container.config.apiSpecPath}' (${container.config.branch})`);
    fetchPages();
    bundleSpec();
    setupUI();

    log.log(`Done (in ${Math.floor(process.uptime())}s.)`);

    return { };
  } catch (err) {
    const { log } = container;
    log ? log.error(err.message || err) : console.error(err); // eslint-disable-line no-console
    throw err;
  }
};

export default runTasks;
