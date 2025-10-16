# Tapis Jobs

### Tapis Jobs service
Tapis Job service aims at launching applications directly on hosts or as job submitted to schedulers (currently only Slurm).
The Tapis v3 Jobs service is specialized to run containerized applications on any host that supports container runtimes.
Currently, Docker and Singularity containers are supported. The Jobs service uses the Systems, Apps, Files and Security
Kernel services to process jobs.


### Life cycle of Jobs
When a job request is received as the payload of an POST call, the following steps are taken:

* **Request authorization** - The tenant, owner, and user values from the request and Tapis JWT are used to authorize access to the application, execution system and, if specified, archive system.
* **Request validation** - Request values are checked for missing, conflicting or improper values; all paths are assigned; required paths are created on the execution system; and macro substitution is performed to finalize all job parameters.
* **Job creation** - A Tapis job object is written to the database.
* **Job queuing** - The Tapis job is queue on an internal queue serviced by one or more Job Worker processes.
* **Response** - The initial Job object is sent back to the caller in the response. This ends the synchronous portion of job submission.

After these synchronous steps job processing proceeds asynchronously. Each job is assigned a worker thread and job proceeds until it completes successfully, fails or gets blocked.


### Job Status
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


Simple job submission example:
```
job_response_vm=client.jobs.submitJob(name='sentiment analysis',description='sentiment analysis with hugging face transformer pipelines',appId=app_id,appVersion='0.2',execSystemId=system_id_vm, **pa)

```
* **appId**	- The Tapis application to execute.  This must be a valid application that the user has permission to run.
* **name**	-  The user selected name for the job.
* **appVersion** - The version of the application to execute.
* **execSystemId** - Tapis execution system ID. It can be inherited from the app
* **parameterSet**	-	Runtime parameters organized by category
 <br/>
**appId**, **name** and **appVersion** are required parameters.

Please refer to all the job submission parameters here [Job Submission Parameters](https://tapis.readthedocs.io/en/latest/technical/jobs.html#the-job-submission-request)


### Exercise: Running mpm app on VM

## Application Arguments
With appArgs parameter you  can specify one or more command line arguments for the user application. <br/>
Arguments specified in the application definition are appended to those in the submission request. Metadata can be
attached to any argument.<br/>


### Submit a job on VM Host

```
#Submit job to run the sentiment analysis application
pa= {
    "parameterSet": {
    "appArgs": [
            {"arg": "--sentences"},
            {"arg": "\"This is great\" \"This is not fun\""}
            
        ]
    }}

# Submit a job
job_response_vm=client.jobs.submitJob(name='sentiment analysis',description='sentiment analysis with hugging face transformer pipelines',appId=app_id,appVersion='0.1',execSystemId=system_id_vm, **pa)


```

Everytime a job is submitted, a unique job id (uuid) is generated. We will use this job id with tapipy to get the job
status, and download the job output.

```
# Get job uuid from the job submission response
print("****************************************************")
job_uuid_vm=job_response_vm.uuid
print("Job UUID: " + job_uuid_vm)
print("****************************************************")

```

### Jobs List
Now, when you do a jobs-list now, you can see your jobUuid.

```
client.jobs.getJobList()

```

### Jobs Status
Job status allows you to see the current state of the job.

```  python
# Check the status of the job
print("****************************************************")
print(client.jobs.getJobStatus(jobUuid=job_uuid_vm))
print("****************************************************")

```
Job enters into different states throughout the execution. Details about different job states are given here [JOB STATES](https://tapis.readthedocs.io/en/latest/technical/jobs.html#job-status)


### Jobs Output
To download the output of job you need to give it jobUuid and output path. You can download a directory in the jobs’ outputPath in zip format. The outputPath is relative to archive system specified.


``` python
# Download output of the job
print("Job Output file:")

print("****************************************************")
jobs_output_vm= client.jobs.getJobOutputDownload(jobUuid=job_uuid_vm,outputPath='stdout')
print(jobs_output_vm)
print("****************************************************")
```


### What's next?

If you made it this far, you have successfully created a new app within a container and have deployed that tool on an
HPC like system, and now you can run that tool through the cloud from anywhere!  That is quite a lot in one workshop.

At this point, it would be a good idea to connect with other developers that are publishing apps and running workflows
through Tapis by joining the Tapis API Slack channel: [tacc-cloud.slack.com](https://bit.ly/2XHYJEk)



