import pkg from '../../package.json';
import Log from './log';

const log = new Log();

const helpText = `Cloud Schema Docs - v${pkg.version}
  Usage: cloud-schema-docs [options]
  -c --config            Path to local configuration options [default: ".spec-docs.json"]
  -d --dry-run           Do not touch or write anything, but show the commands
  -h --help              Print this help
  -v --version           Print version number
  -V --verbose           Verbose output`;

const version = () => log.log(`v${pkg.version}`);
const help = () => log.log(helpText);
export { version, help };