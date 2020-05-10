import { version, help } from './cli';
import runTasks from './tasks';

const release = async options =>  {
  if (options.version) {
    version();
  } else if (options.help) {
    help();
  } else {
    return runTasks();
  }
  return Promise.resolve();
}

export default release;