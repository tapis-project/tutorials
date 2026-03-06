# Tapis Applications

In order to run a job on a system you will need to create or have access to a Tapis **application**. Note that
an application in Tapis is not tied to a particular system and can be shared among users in the tenant.

## Overview
A Tapis application represents all the information required to run a Tapis job on a Tapis system and produce useful
results. Each application is versioned and is associated with a specific tenant and owned by a specific user who has
special privileges for the application. In order to support this purpose an application definition includes information
which allows the *Jobs* service to:
* Stage input prior to launching the application
* Launch the application
* Monitor the application during execution
* Archive output after application execution

## Versioning
Applications are expected to evolve over time. An initial version will be created and may enjoy widespread use. When
the application must be modified it is important to allow for previous versions of the application to be used while new
versions are created and tested.

The versioning scheme is at the discretion of the application author. The combination of ``tenant+id+version`` uniquely
identifies an application in the Tapis environment. It is recommended that a two or three level form of
semantic versioning be used. The fully qualified application reference within a tenant is constructed by appending
a hyphen to the name followed by the version string. For example, the first two versions of an application might
be *myapp-0.0.1* and *myapp-0.0.2*. If a version is not specified when retrieving an application then by default the most
recently created version of the application will be returned.

## Model
An application contains some information that is independent of the version and some information that varies by version.
At a high level an application represents the following information:

### Non-Versioned Attributes

* **id** - A short descriptive name for the application that is unique within the tenant.
* **owner** - A specific user set at application creation. Default is ``${apiUserId}``, the user making the request to create the application.

### Versioned Attributes

* **version** - Applications are expected to evolve over time. ``Id`` + ``version`` must be unique within a tenant.
* **description** - An optional more verbose description for the application.
* **runtime** - Runtime to be used when executing the application. DOCKER, SINGULARITY, ZIP. Default is DOCKER.
* **containerImage** - Reference to be used when running the container image.
* **maxJobs** - Maximum total number of jobs that can be queued or running for this application on a given execution  
  system at a given time. Set to -1 for unlimited.
* **maxJobsPerUser** - Maximum total number of jobs associated with a specific job owner that can be queued or running for
  this application. Set to -1 for unlimited.
* **strictFileInputs** -  Flag indicating if a job request is allowed to have unnamed file inputs. 
* **Job related attributes** - Various attributes related to job execution such as *execSystemId*, *parameterSet*, *archiveFilter*, etc.

For more information about applications and the Applications service please see [Tapis Applications Service documentation](https://tapis.readthedocs.io/en/latest/technical/apps.html).

## Getting Started

Here we review how to create an application and how to retrieve application details. In the examples below we assume you are using Tapis UI ``https://public.tapis.io`` and that you have authenticated using your TACC credentials and token.

### Creating a FlexServ Application

The following app is used to run the FlexServer on TACC's Vista System. For the purposes of this tutorial, the application has already been registered with Tapis and is available as a public app for all users to submit jobs.

It is important to note that when users register a new application, it is ``private`` by default and accessible only to the ``owner``. Authors then have the flexibility to share the application with specific users or make it publicly available across the entire tenant.

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
This is how one can register app directly from Tapis UI. **Note: App is already registered for this tutorial**
![App Create with Tapis UI](/tutorials/images/TapisUI_App.png)

You should see the Flex Server application already registered in your Tapis UI: **FlexServ-vista-nairr version 1.4.0**
![FlexServ Application](/tutorials/images/Flexserv_app.png)

We will now move to the [Jobs](./04-jobs.md) to run this application.

### Creating a Ultralytics Fine tuning Application



## Next Steps
Now that we have our very first application ready to use, we are ready to run it on a system using the Jobs service. 

[Next-> Jobs](./04-jobs.md)
