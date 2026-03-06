## Adding TMS Credentials on the Vista system.

Todo:


## Running FlexServ Application on Vista

The following app runs the FlexServer on TACC's Vista System. For the purposes of this tutorial, the application has already been registered with Tapis and is available as a public app for all users to submit jobs.

``` python
app_def = {
    "id": "FlexServ-vista-nairr",
    "version": "1.3.0",
    "description": "A TACC-owned inference server for running AI models.",
    "owner": "${apiUserId}",
    "enabled": True,
    "runtime": "ZIP",
    "runtimeOptions": ["SINGULARITY_RUN"],
    "containerImage": "[https://github.com/tapis-project/FlexServ-Deployer/releases/download/tapis-flexserv-1.3.0/Tapis-FlexServ.zip](https://github.com/tapis-project/FlexServ-Deployer/releases/download/tapis-flexserv-1.3.0/Tapis-FlexServ.zip)",
    "jobType": "BATCH",
    "maxJobs": -1,
    "maxJobsPerUser": -1,
    "strictFileInputs": True,
    "jobAttributes": {
        "description": "FlexServ run by ${JobOwner}",
        "dynamicExecSystem": False,
        "execSystemExecDir": "${JobWorkingDir}",
        "execSystemInputDir": "${JobWorkingDir}",
        "execSystemOutputDir": "${JobWorkingDir}/output",
        "execSystemLogicalQueue": "debug",
        "archiveSystemDir": "HOST_EVAL($WORK)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}",
        "archiveMode": "ALWAYS",
        "parameterSet": {
            "appArgs": [
                {
                    "name": "flexServPort",
                    "arg": "--flexserv-port 8000",
                    "inputMode": "INCLUDE_ON_DEMAND"
                },
                {
                    "name": "modelName",
                    "arg": "--model-name Qwen/Qwen3-0.6B",
                    "inputMode": "INCLUDE_ON_DEMAND"
                }
            ],
            "schedulerOptions": [
                {
                    "name": "TACC Scheduler Profile",
                    "arg": "--tapis-profile tacc-apptainer",
                    "inputMode": "FIXED"
                }
            ],
            "envVariables": [
                {
                    "key": "HUGGINGFACE_TOKEN",
                    "value": "",
                    "inputMode": "INCLUDE_ON_DEMAND"
                }
            ],
            "archiveFilter": { "includeLaunchFiles": True }
        },
        "nodeCount": 1,
        "coresPerNode": 1,
        "memoryMB": 256000,
        "maxMinutes": 10
    },
    "notes": {
        "label": "FlexServ",
        "category": "Utilities",
        "dynamicExecSystems": ["vista", "stampede3", "ls6"]
    }
}
```

You should see the Flex Server application already registered in your Tapis UI: **FlexServ-vista-nairr version 1.4.0**
![FlexServ Application](/tutorials/images/Flexserv_app.png)

## Submit FlexServ Job using TAPIS UI

**1. Initiate Submission**

In the Tapis UI, navigate to the application **FlexServ-vista-nairr**, click the Submit Job button, and select **SUBMIT WITH JSON**.

![Step 1: Select Submit with JSON](/tutorials/images/Step1-submit-with-json.png)

**2. Configure the Payload**

Replace the default JSON in the editor with your specific configuration. Copy the json below in the editor and make sure to edit the Project Allocation name that we have provided.

![Step 2: Job Json](/tutorials/images/Step2-paste-json.png)

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
![Step 3: Job Submit](/tutorials/images/Step3-submitjob.png)


**4. View Job**

Once job is submitted successfully, you should go to the left panel and in core services click on job. You can see in some time that your job has entered running state, as shown in the image below.

![Step 4: Job running](/tutorials/images/Jobrunning.png)


**5. View Job Output file to get the Flex server port and Token**

Step 5a) Click on tapisjob.out file and then click view. This should open the file for vieweing
![Step 5a: Job output file](/tutorials/images/ViewTapisjobout.png)

Step 5b) Once the file opens, look at the ACCESS INFORMATION Section to grab the url for your flex server with port number and also the TAP token. Save it to your notepad.
![Step 5b: Vista_url_token](/tutorials/images/GetFlexServerPortToken.png)


### What's next?

If you made it this far, you have successfully created a new flex serv app, you can explore the Flexserv UI and try to send your first chat

### Using the Flexserv UI 
Todo: 
* Setting the Flexserv API Key and Sending your first chat 
* Public and Private Model Pools 
* Working with Images 
* Working with Some other Examples 
