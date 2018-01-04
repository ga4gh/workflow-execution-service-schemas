## Overview

Let's use this to collect feedback from drivers

## HCA

* definition of a workflow: 1) workflow descriptor, 2) execution of a workflow, 3) pre-defined workflow on a system.
* workflow_params: doesn’t fit in with WDL... JSON you give a WDL executor is not typed, just strings.  
    * AI: can we have File and Directory type in WDL JSON param file, see pull request
* env specific param
    * requirements for disk, memory, cpu
    * workflow options... these are used by cromwell as a service
* argument in workflow_params... should be string not struct
* zip file for workflow_descriptor?
    * workflow_descriptor... support zip file
* 200 responses... everything response to this... some things we need swagger to tell 
* credentials for downloading things
