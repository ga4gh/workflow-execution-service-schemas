import _ from 'lodash';
import path from 'path';
import envConfig from './environment';
import fs from 'fs';
/*eslint no-process-env:0*/

// All configurations will extend these options
// ============================================
const userConfigPath = `${envConfig.root}/.spec-docs.json`;
const userConfig = fs.existsSync(userConfigPath) ? JSON.parse(fs.readFileSync(userConfigPath)) : {};
const localConfig = {
  apiSpecPath: userConfig.apiSpecPath || '',
  docsRoot: userConfig.docsRoot || 'docs',
  uiRoot: userConfig.uiRoot || 'swagger-ui',
  redocRoot: userConfig.redocRoot || 'redoc-ui',
  defaultBranch: userConfig.defaultBranch || 'master',
  branchPathBase: userConfig.branchPath || 'preview',
  contactUrl: userConfig.contactUrl || ''
};

const constructBranchPath = (defaultBranch, currentBranch, root, branchPathBase) => {
  if (currentBranch == defaultBranch) {
    return root;
  } else {
    return path.join(root, branchPathBase, currentBranch.toLowerCase())
  }
};

const deployConfig = {
  branchPath: constructBranchPath(
    localConfig.defaultBranch,
    envConfig.branch,
    envConfig.root,
    localConfig.branchPathBase
  )
};
// Export the config object based on the NODE_ENV
// ==============================================
const config = _.merge(
  localConfig,
  envConfig,
  deployConfig
);

console.log(config);
export default config;