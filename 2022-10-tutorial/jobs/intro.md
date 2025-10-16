# Introduction to Tapis Jobs service
Tapis Job service aims at launching applications directly on hosts or as job submitted to schedulers (currently only Slurm).
The Tapis v3 Jobs service is specialized to run containerized applications on any host that supports container runtimes.
Currently, Docker and Singularity containers are supported. The Jobs service uses the Systems, Apps, Files and Security
Kernel services to process jobs.

## Life cycle of Jobs
When a job request is received as the payload of an POST call, the following steps are taken:

* **Request authorization** - The tenant, owner, and user values from the request and Tapis JWT are used to authorize access to the application, execution system and, if specified, archive system.
* **Request validation** - Request values are checked for missing, conflicting or improper values; all paths are assigned; required paths are created on the execution system; and macro substitution is performed to finalize all job parameters.
* **Job creation** - A Tapis job object is written to the database.
* **Job queuing** - The Tapis job is queue on an internal queue serviced by one or more Job Worker processes.
* **Response** - The initial Job object is sent back to the caller in the response. This ends the synchronous portion of job submission.

After these synchronous steps, job processing proceeds asynchronously. Each job is 
assigned a worker thread and job proceeds until it completes successfully, fails or gets 
blocked.

## Job Status
Jobs move through the following statuses during their lifetime:

**PENDING** - Job processing beginning <br/>
**PROCESSING_INPUTS** - Identifying input files for staging <br/>
**STAGING_INPUTS** - Transferring job input data to execution system <br/>
**STAGING_JOB** - Staging runtime assets to execution system <br/>
**SUBMITTING_JOB** - Submitting job to execution system <br/>
**QUEUED** - Job queued to execution system queue <br/>
**RUNNING** - Job running on execution system <br/>
**ARCHIVING** - Transferring job output to archive system <br/>
**BLOCKED** - Job blocked <br/>
**PAUSED** - Job processing suspended <br/>
**FINISHED** - Job completed successfully <br/>
**CANCELLED** - Job execution intentionally stopped <br/>
**FAILED** - Job failed <br/>


## A Minimal Job
A minimal job submission example looks like this:
```
{
    "name": "myJob",
    "appId": "myApp",
    "appVersion": "1.0"

}
```
where:
* **appId**	- The Tapis application to execute.  This must be a valid application that the user has permission to run.
* **name**	-  The user selected name for the job.
* **appVersion** - The version of the application to execute.

A few additional arguments that often get used are: 
* **execSystemId** - Tapis execution system ID. It can be inherited from the app
* **parameterSet**	-	Runtime parameters organized by category
 <br/>
**appId**, **name** and **appVersion** are required parameters.

The complete set of job submission parameters are listed here [Job Submission Parameters](https://tapis.readthedocs.io/en/latest/technical/jobs.html#the-job-submission-request)