<img src="https://www.ga4gh.org/gfx/GA-logo-horizontal-tag-RGB.svg" alt="GA4GH Logo" style="width: 400px;"/>

Workflow Execution Service (WES) API
====================================

[![Build Status](https://travis-ci.org/ga4gh/workflow-execution-service-schemas.svg?branch=master)](https://travis-ci.org/ga4gh/workflow-execution-service-schemas)
<img src="http://online.swagger.io/validator?url=https://raw.githubusercontent.com/ga4gh/workflow-execution-service-schemas/develop/openapi/workflow_execution_service.swagger.yaml" alt="Swagger Validator" style="height:15pt;">

The [Global Alliance for Genomics and Health](http://genomicsandhealth.org/) is an international coalition, formed to enable the sharing of genomic and clinical data.

Cloud Work Stream
-----------------

The [Cloud Work Stream](https://ga4gh/cloud) helps the genomics and health communities take full advantage of modern cloud environments. Our initial focus is on “bringing the algorithms to the data”, by creating standards for defining, sharing, and executing portable workflows. We work with platform development partners and industry leaders to develop standards that will facilitate interoperability.

What is WES?
============

The Workflow Execution Service API describes a standard programmatic way to run and manage workflows. Having this standard API supported by multiple execution engines will let people run the same workflow using various execution platforms running on various clouds/environments.

Key features include:

* ability to request a workflow run using CWL or WDL
* ability to parameterize that workflow using a JSON document
* ability to get information about running workflows

API Definition
--------------

See the human-readable [Reference Documentation](https://ga4gh.github.io/workflow-execution-service-schemas/docs/) 
and the [OpenAPI description](openapi/workflow_execution_service.swagger.yaml). You can also explore the specification in [Swagger UI](http://ga4gh.github.io/workflow-execution-service-schemas/swagger-ui/).


Use Cases
---------

Use cases include:

* "Bring your code to the data": a researcher who has built their own custom analysis can submit it to run on a dataset owned by an external organization, instead of having to make a copy of the data
* Best-practices pipelines: a researcher who maintains their own controlled data environment can find useful workflows in a shared directory (e.g. [Dockstore.org](http://dockstore.org)), and run them over their data

Possible Future Enhancements
----------------------------
* common JSON parameterization format that works with CWL and WDL
* validation service for testing WES implementations' conformance to the spec
* improved tools for troubleshooting execution failures, especially when there are 100s-1000s of tasks
* a callback mechanism for monitoring status changes in running workflows (e.g. a webhook)
* integration with GA4GH data access APIs (e.g. htsget, DOS)

How to View
------------
- Documentation: https://ga4gh.github.io/workflow-execution-service-schemas/docs/
- Swagger UI: https://ga4gh.github.io/workflow-execution-service-schemas/swagger-ui/
- Full API specification:
    + JSON https://ga4gh.github.io/workflow-execution-service-schemas/swagger.json
    + YAML https://ga4gh.github.io/workflow-execution-service-schemas/swagger.yaml
- Preview versions of docs, Swagger UI, or spec for branch `[branch]`:
    + https://ga4gh.github.io/workflow-execution-service-schemas/preview/[branch]/docs/
    + https://ga4gh.github.io/workflow-execution-service-schemas/preview/[branch]/swagger-ui/
    + https://ga4gh.github.io/workflow-execution-service-schemas/preview/[branch]/swagger.json
    + https://ga4gh.github.io/workflow-execution-service-schemas/preview/[branch]/swagger.yaml

How to Contribute Changes
-------------------------

See [CONTRIBUTING.md](CONTRIBUTING.md).
If a security issue is identified with the specification, please send an email to security-notification@ga4gh.org detailing your concerns.

License
-------

See the [LICENSE](LICENSE).

More Information
----------------

* [Global Alliance for Genomics and Health](http://genomicsandhealth.org)
* [GA4GH Cloud Work Stream](https://ga4gh.cloud)
