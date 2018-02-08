<img src="https://www.ga4gh.org/gfx/GA-logo-horizontal-tag-RGB.svg" alt="GA4GH Logo" style="width: 100px;"/>

Schemas for the Workflow Execution Service (WES) API
====================================================

The [Global Alliance for Genomics and Health](http://genomicsandhealth.org/) is an international
coalition, formed to enable the sharing of genomic and clinical data.

Cloud Work Stream
-----------------

The [Cloud Work Stream](https://ga4gh/cloud) concentrates on data representation, storage,
and analysis, including working with platform development partners and
industry leaders to develop standards that will facilitate
interoperability.  The Cloud Work Stream is an informal, multi-vendor working group focused on standards for exchanging Docker-based tools and CWL/WDL workflows, execution of Docker-based tools and workflows on clouds, and abstract access to cloud object stores.

What is WES?
============

The Workflow Execution Schema is a minimal common API describing how a user can submit
workflow requests to workflow execution systems in standardized ways.
Workflow execution engines (SevenBridges, FireCloud, etc) can support this API so users can make workflow requests
programmatically, adding the ability to scale up.  In addition, these workflow services could have (and probably do have)
UIs that would (possibly) use this API under the hood to facilitate workflow execution requests.

Having this standard API supported by multiple execution engines will give people options of processing
the same workflow (CWL or WDL) across different workflow execution platforms running across various clouds/environments.
As an example use case, one can find a workflow in CWL on [Dockstore.org](http://dockstore.org), use Dockstore to
generate a JSON parameterization file, and submit this to a GA4GH-compliant
workflow execution service.

Key features of the current API proposal:

* ability to request a workflow run using CWL or WDL (and maybe future formats)
* ability to parameterize that workflow using a JSON schema (ideally a future version would be in common between CWL and WDL)
* ability to get information about running workflows, status, errors, output file locations, etc.
* to search for workflows by arbitrary key/values

Outstanding questions:

* a common JSON parameterization format
* standardizing terms, job, workflow, steps, tools, etc
* reference implementation at https://github.com/common-workflow-language/cwltool-service/tree/ga4gh-wes
* validation service for testing WES implementations' conformance to the spec
* Including all task_logs in the workflow log request may present a scaling problem when there are 100s-1000s of tasks
* Providing a state notification callback URL (eg a webhook)
* Passing through authentication (user role)

How to view
------------

The file `swagger/workflow_execution_service.swagger.json` contains the API description.

Please visit http://ga4gh.github.io/workflow-execution-service-schemas to view this document in Swagger UI.

Building Documents
------------------

Make sure you have Docker installed for your platform and the `cwltool`.

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

You can generate the [Swagger](http://swagger.io/) from the Protocol Buffers:

    cwltool CWLFile
    sh tools/prepare_openapi.sh

The resulting OpenAPI description will be in the `swagger` directory.

How to contribute changes
-------------------------

Take cues for now from the [ga4gh/schemas](https://github.com/ga4gh/schemas/blob/master/CONTRIBUTING.rst) document.

We like [HubFlow](https://datasift.github.io/gitflow/) and using pull requests to suggest changes.

License
-------

See the [LICENSE]

More Information
----------------

* [Global Alliance for Genomics and Health](http://genomicsandhealth.org)
* [GA4GH Cloud Work Stream)[https://ga4gh.cloud]
