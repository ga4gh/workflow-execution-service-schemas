![ga4gh logo](http://genomicsandhealth.org/files/logo_ga.png)

Schemas for the Workflow Execution Service (WES) API
====================================================

This is used by the Data Working Group - Containers and Workflows Task Team

<img src="swagger_editor.png" width="48">[View in Swagger](http://editor.swagger.io/#/?import=https://raw.githubusercontent.com/ga4gh/workflow-execution-schemas/0.1.0/swagger/proto/workflow_execution.swagger.json)

The [Global Alliance for Genomics and Health](http://genomicsandhealth.org/) is an international
coalition, formed to enable the sharing of genomic and clinical data.

Containers and Workflows Task Team
----------------------------------

The [Data Working Group](http://ga4gh.org/#/) concentrates on data representation, storage,
and analysis, including working with platform development partners and
industry leaders to develop standards that will facilitate
interoperability.  The Containers & Workflows working group is an informal, multi-vendor working group focused on standards for exchanging Docker-based tools and CWL/WDL workflows, execution of Docker-based tools and workflows on clouds, and abstract access to cloud object stores.

What is WES?
============
The Containers & Workflows working group is an informal, multi-vendor working group born out of the BOSC 2014 codefest, consisting of various organizations and individuals that have an interest in portability of data analysis workflows. Our goal is to create specifications that enable data scientists to describe analysis tools and workflows that are powerful, easy to use, portable, and support reproducibility for a variety of problem areas including data-intensive science like bioinformatics, physics, and astronomy; and business analytics such as log analysis, data mining, and ETL.

What is this?
-------------

Currently, this is the home of the Workflow Execution API proposal. The Workflow Execution API is a minimal common API describing how a user can submit workflow requests to workflow execution systems in a standardized ways.
Workflow execution engines (SevenBridges, FireCloud, etc) can support this API so users can make workflow requests
programmatically, adding the ability to scale up.  In addition, these workflow services could have (and probably do have)
UIs that would (possibly) use this API under the hood to facilitate workflow execution requests.

Having this standard API supported by multiple execution engines will give people options of processing
the same workflow (CWL or WDL) across different workflow execution platforms running across various clouds/environments.
As an example use case, I can find a workflow in CWL on [Dockstore.org](http://dockstore.org), use Dockstore to
generate a JSON parameterization file, and submit this to SevenBridges/FireCloud/Consonance or some other GA4GH-compliant
workflow execution service.  NOTE: I'm making the leap of faith here that SevenBridges/FireCloud and/or other
systems support this API, this example is not an endorsement or commitment to support the API by these
providers, just an example of how that would work if they did.

Key features of the current API proposal:

* ability to request a workflow run using CWL or WDL (and maybe future formats)
* ability to parameterize that workflow using a JSON schema (ideally a future version would be in common between CWL and WDL)
* ability to get information about running workflows, status, errors, output file locations etc
* to search for workflows by arbitrary key/values

Outstanding questions:

* a common JSON parameterization format, see work by Peter, is that checked in?
* standardizing terms, job, workflow, steps, tools, etc
* reference implementation, Peter pointed out https://github.com/common-workflow-language/cwltool-service/tree/ga4gh-wes
* validation service for testing WES implementations' conformance to the spec

How to view
------------

See the swagger editor to view our [schema in progress](http://editor.swagger.io/#/?import=https://raw.githubusercontent.com/ga4gh/workflow-execution-schemas/develop/src/main/resources/swagger/ga4gh-tool-discovery.yaml).

If the current schema fails to validate, visit [debugging](http://online.swagger.io/validator/debug?url=https://raw.githubusercontent.com/ga4gh/workflow-execution-schemas/develop/src/main/resources/swagger/ga4gh-tool-discovery.yaml)

Building Documents
------------------

Make sure you have Docker installed for your platform and the `cwltool`.

    virtualenv env
    source env/bin/activate
    pip install setuptools==28.8.0
    pip install cwl-runner cwltool==1.0.20161114152756 schema-salad==1.18.20161005190847 avro==1.8.1

Make sure you have the [submodule](http://stackoverflow.com/questions/3939055/submodules-files-are-not-checked-out) checked out:

    git submodule update --init --recursive

You can generate the [Swagger](http://swagger.io/) YAML from the Protocol Buffers:

    cwltool CWLFile

Find the output in `workflow_execution.swagger.json` and this can be loaded in the [Swagger editor](http://swagger.io/swagger-editor/).  Use the GitHub raw feature to generate a URL you can load.

When you're happy with the changes, checkin this file:

    mv workflow_execution.swagger.json swagger/proto/

And commit your changes.

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
* [Google Forum](https://groups.google.com/forum/#!forum/ga4gh-dwg-containers-workflows)
