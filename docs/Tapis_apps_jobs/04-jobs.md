# Tapis Jobs

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
* **PENDING** - Job processing beginning
* **PROCESSING_INPUTS** - Identifying input files for staging
* **STAGING_INPUTS** - Transferring job input data to execution system
* **STAGING_JOB** - Staging runtime assets to execution system
* **SUBMITTING_JOB** - Submitting job to execution system
* **QUEUED** - Job queued to execution system queue
* **RUNNING** - Job running on execution system
* **ARCHIVING** - Transferring job output to archive system
* **BLOCKED** - Job blocked
* **PAUSED** - Job processing suspended
* **FINISHED** - Job completed successfully
* **CANCELLED** - Job execution intentionally stopped
* **FAILED** - Job failed

---

### Exercise: Running FlexServ on Vista

#### Application Arguments
With the `appArgs` parameter, you can specify one or more command line arguments for the user application. Arguments specified in the application definition are appended to those in the submission request.

#### Submit a job via TAPIS UI


**1. Initiate Submission**

In the Tapis UI, navigate to the application **FlexServ-vista-nairr**, click the Submit Job button, and select **SUBMIT WITH JSON**.

![Step 1: Select Submit with JSON](/docs/images/Step1-submit-with-json.png)

**2. Configure the Payload**

Replace the default JSON in the editor with your specific configuration. Copy the json below in the editor and make sure to edit the Project Allocation name that we have provided.

![Step 2: Job Json](/docs/images/Step2-paste-json.png)

```json
{
  "name": "tap_flexserv_vista_test",
  "appId": "FlexServ-vista-nairr",
  "appVersion": "1.4.0",
  "execSystemId": "vista-test-nairr",
  "tenant": "public",
  "execSystemLogicalQueue": "gh",
  "maxMinutes": 60,
  "parameterSet": {
    "appArgs": [
      {
        "arg": "--flexserv-port 8000",
        "name": "flexServPort"
      },
      {
        "arg": "--model-name Qwen/Qwen2.5-Coder-0.5B",
        "name": "modelName"
      },
      {
        "arg": "--enable-https",
        "name": "enableHttps"
      },
      {
        "arg": "--device auto",
        "name": "device"
      },
      {
        "arg": "--dtype bfloat16",
        "name": "dtype"
      },
      {
        "arg": "--attn-implementation sdpa",
        "name": "attnImplementation"
      },
      {
        "arg": "--model-timeout 86400",
        "name": "modelTimeout"
      },
      {
        "arg": "--quantization none",
        "name": "quantization"
      },
      {
        "arg": "--is-distributed 0",
        "name": "isDistributed"
      }
    ],
    "envVariables": [
      {
        "key": "PRI_MODEL_HOST",
        "value": "HOST_EVAL($SCRATCH)/flexserv/models"
      },
      {
        "key": "PUB_MODEL_HOST",
        "value": "/work/projects/aci/cic/models"
      }
    ],
    "schedulerOptions": [
      {
        "arg": "--tapis-profile tacc-apptainer",
        "name": "TACC Scheduler Profile"
      },
      {
        "name": "Reservation Name",
        "arg": "--reservation GHTapis+Nairr"
      },
      {
        "name": "TACC Resource Allocation",
        "description": "The TACC Allocation associated with this job execution",
        "include": true,
        "arg": "-A << add allocation >>"
      }
    ]
  }
}
```
**3. Submit Job**

Once the job definition is pasted click on Submit job
![Step 3: Job Submit](/docs/images/Step3-submitjob.png)


**4. View Job**

Once job is submitted successfully, you should go to the left panel and in core services click on job. You can see in some time that your job has entered running state, as shown in the image below.

![Step 4: Job running](/docs/images/Jobrunning.png)


**5. View Job Output file to get the Flex server port and Token**

Step 5a) Click on tapisjob.out file and then click view. This should open the file for vieweing
![Step 5a: Job output file](/docs/images/ViewTapisjobout.png)

Step 5b) Once the file opens, look at the ACCESS INFORMATION Section to grab the url for your flex server with port number and also the TAP token. Save it to your notepad.
![Step 5b: Vista_url_token](/docs/images/GetFlexServerPortToken.png)


### What's next?

If you made it this far, you have successfully created a new flex serv app, you can go to the url and explore some of the chat completion and responses API.





