import '@babel/polyfill';
// const updater = require('update-notifier');
import parseArgs from 'yargs-parser';
import pkg from '../package.json';
import release from './lib';

const aliases = {
  c: 'config',
  d: 'dry-run',
  h: 'help',
  v: 'version',
  V: 'verbose'
};

const parseCliArguments = args => {
  const options = parseArgs(args, {
    boolean: ['dry-run'],
    alias: aliases,
    default: {
      'dry-run': false,
      verbose: 0
    },
    count: ['verbose'],
    configuration: {
      'parse-numbers': false
    }
  });
  return options;
}

const options = parseCliArguments([].slice.call(process.argv, 2));
// updater({ pkg: pkg }).notify();
release(options).then(() => process.exit(0), () => process.exit(1));