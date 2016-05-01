#Definition Of Terms

##Job
A *job* represents a single command line invocation by an underlying execution platform such as SGE, LSF, a process on a Unix machine, the Google Genomics Pipeline API, etc. In cases where a command line would not be an appropriate abstraction a *job* would be the most atomic unit of work for that platform.

##Task
A *task* is an abstraction of a *job*. A *task* provides metadata to describe provenance and execution but does not need to be directly runnable. Examples of metadata would be docker image and descriptions of inputs and outputs.

##Workflow
A *workflow* is a composition of one or more *tasks* with information on dependencies and order. A *workflow* will have rich enough metadata to be directly runnable.

##Tool
A *tool* describes a single useful unit of work, ranging from a workflow with a single *task* to one with any arbitrary number of *tasks*. The term *tool* is less of a technical term than a concept for clients and end users. 

Imagine a multi-*task* *workflow* to process sequencing data through variant calling. The author of this *workflow* might view each individual *task* as a *tool* while the end user of that variant calling *workflow* would likely view the entire thing as the *tool*.

