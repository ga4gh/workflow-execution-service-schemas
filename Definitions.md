#Definition Of Terms

##TaskInstance
A *TaskInstance* represents a single command line invocation by an underlying execution platform such as SGE, LSF, a process on a Unix machine, the Google Genomics Pipeline API, etc. In cases where a command line would not be an appropriate abstraction a *TaskInstance* would be the most atomic unit of work for that platform.

##Task
A *task* is an abstraction of a *TaskInstance*. A *task* provides metadata to describe provenance and execution but does not need to be directly runnable. Examples of metadata would be docker image and descriptions of inputs and outputs.

##Workflow
A *workflow* is a composition of one or more *tasks* with information on dependencies and order. A *workflow* will have rich enough metadata to be directly runnable.

##Tool
A *tool* describes a single useful unit of work, ranging from a workflow with a single *task* to one with any arbitrary number of *tasks*. The term *tool* is less of a technical term than a concept for clients and end users and is more generic than other terms in this document. It is recommended that *tool* is not used in any official GA4GH documentation, however the term is so ubiquitious that we recognize others will be using it. Therefore we want to call special attention to how variable its meaning can be.

As an example, imagine a multi-*task* *workflow* to process sequencing data through variant calling. The author of this *workflow* might view each individual *task* as a *tool* while the end user of that variant calling *workflow* would likely view the entire thing as the *tool*.

