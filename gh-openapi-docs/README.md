# gh-openapi-docs

## Installation

Install command-line dependencies:

```shell
npm install -g @redocly/openapi-cli && npm install -g redoc-cli
```

Install CLI:

```shell
npm install -g gh-openapi-docs
```

## Set up

Within a repo directory that contains an OpenAPI spec, create a config file named `.spec-docs.json` with the relative path to your spec:

```json
{
    "apiSpecPath": "openapi/openapi.yaml",
    "contactUrl": ""
}
```

**Note:** an OpenAPI spec for testing can be found at [`test/test-spec/combined/openapi.yaml`](test/test-spec/combined/openapi.yaml).

## Outputs

This package is designed to create artifacts in the following path(s):

- `{branchPath}/docs/index.html`
- `{branchPath}/openapi.json`
- `{branchPath}/openapi.yaml`

Where `branchPath` is the repo root if the current branch is `master`, otherwise `preview/<branchName>`.

## Usage

Run the command...

```shell
gh-openapi-docs
```

You should see console logs that look like this:

```shell
{ apiSpecPath: 'openapi/openapi.yaml',
  docsRoot: 'docs',
  uiRoot: 'swagger-ui',
  redocRoot: 'redoc-ui',
  defaultBranch: 'master',
  branchPathBase: 'preview',
  contactUrl: '',
  sha: '<commit-sha>',
  abbreviatedSha: '<abbreviated-commit-sha>',
  branch: 'develop',
  tag: null,
  committer: 'James Eddy <james.a.eddy@gmail.com>',
  committerDate: '2020-03-13T05:25:03.000Z',
  author: 'James Eddy <james.a.eddy@gmail.com>',
  authorDate: '2020-03-13T05:25:03.000Z',
  commitMessage: 'replace swagger-ui and docs with redoc (for both)',
  root: '<repo-path>',
  commonGitDir: '<repo-path>/.git',
  worktreeGitDir: '<repo-path>/.git',
  lastTag: null,
  commitsSinceLastTag: 0,
  env: undefined,
  repoOrigin:
   'https://github.com/<gh-org>/<repo-name>',
  branchPath:
   '<repo-path>/preview/develop' }

Preparing docs for API spec at 'openapi/openapi.yaml' (develop)
Cloning 'gh-pages' branch into '<repo-path>/.ghpages-tmp'
Cloning into '.'...
...
Branch folder:
<repo-path>/preview/use-redoc
Spec location:
<repo-path>/openapi/openapi.yaml

Bundling API spec...
Storing to:
<repo-path>/preview/develop/openapi.json

> <repo-name>-openapi-spec@1.0.0 swagger <repo-path>
> swagger-repo "bundle" "-o" "<repo-path>/preview/develop/openapi.json"

Created "<repo-path>/preview/develop/openapi.json" openapi file.

> <repo-name>-openapi-spec@1.0.0 swagger <repo-path>
> swagger-repo "bundle" "--yaml" "-o" "<repo-path>/preview/develop/openapi.yaml"

Created "<repo-path>/preview/develop/openapi.yaml" openapi file.
Generating OpenAPI docs index at '<repo-path>/preview/develop/docs/index.html'

> <repo-name>-openapi-spec@1.0.0 redoc <repo-path>
> redoc-cli "bundle" "<repo-path>/preview/develop/openapi.yaml" "--output" "<repo-path>/preview/develop/docs/index.html"

Prerendering docs

🎉 bundled successfully in: <repo-path>/preview/use-redoc/docs/index.html (957 KiB) [⏱ 0.234s]
OpenAPI docs folder contents:
index.html

Done (in 13s.)
```
