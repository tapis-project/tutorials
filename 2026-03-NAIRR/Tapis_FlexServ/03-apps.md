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

```json
{
  "id": "FlexServ-vista-nairr",
  "version": "1.4.0",
  "description": "A TACC-owned inference server for running AI models.",
  "owner": "${apiUserId}",
  "enabled": true,
  "runtime": "ZIP",
  "runtimeVersion": null,
  "runtimeOptions": [
    "SINGULARITY_RUN"
  ],
  "containerImage": "https://github.com/tapis-project/FlexServ-Deployer/releases/download/tapis-flexserv-1.4.0/Tapis-FlexServ.zip",
  "jobType": "BATCH",
  "maxJobs": -1,
  "maxJobsPerUser": -1,
  "strictFileInputs": true,
  "jobAttributes": {
    "description": "FlexServ run by ${JobOwner}",
    "dynamicExecSystem": false,
    "execSystemConstraints": null,
    "execSystemExecDir": "${JobWorkingDir}",
    "execSystemInputDir": "${JobWorkingDir}",
    "execSystemOutputDir": "${JobWorkingDir}/output",
    "execSystemLogicalQueue": "debug",
    "archiveSystemDir": "HOST_EVAL($WORK)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}",
    "archiveMode": "ALWAYS",
    "isMpi": false,
    "mpiCmd": null,
    "cmdPrefix": null,
    "parameterSet": {
      "appArgs": [
        {
          "name": "flexServPort",
          "description": "The port on which the FlexServ server will listen. If not specified, it will default to 8000. If any conflict occurs with the port you specified, our bootloader will automatically select another available port and you can check job logs to see which port is actually used.",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--flexserv-port 8000"
        },
        {
          "name": "flexServSecret",
          "description": "This is the secret string used for authentication when you access the FlexServ server. You can change it to whatever you want, but make sure to use the same string when you access the server. If you don't set it, it will be a TAP Token generated by TAP functions and you can check job logs to see what it is.",
          "inputMode": "INCLUDE_ON_DEMAND",
          "arg": "--secret flexserv"
        },
        {
          "name": "modelName",
          "description": "The name of the default model to be used by the FlexServ server.",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--model-name Qwen/Qwen3.5-0.8B"
        },
        {
          "name": "loginPort",
          "description": "The port to use for login, if specified, we will forcibly use this port for the login node and set up port forwarding from the compute node to this port. If not specified, we will have TAP functions select a port and you have to check job logs to see which port is used for login.",
          "inputMode": "INCLUDE_ON_DEMAND",
          "arg": "--login-port 63210"
        },
        {
          "name": "enableHttps",
          "description": "Enable HTTPS for the FlexServ server.",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--enable-https"
        },
        {
          "name": "device",
          "description": "Device backend hint (default: auto).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--device auto"
        },
        {
          "name": "dtype",
          "description": "Model dtype passed to backend (default: bfloat16).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--dtype bfloat16"
        },
        {
          "name": "attnImplementation",
          "description": "Attention implementation passed to backend (default: sdpa).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--attn-implementation sdpa"
        },
        {
          "name": "modelTimeout",
          "description": "Model timeout seconds passed to backend (default: 86400).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--model-timeout 186400"
        },
        {
          "name": "quantization",
          "description": "Quantization mode passed to backend (default: none).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--quantization none"
        },
        {
          "name": "isDistributed",
          "description": "Indicates whether the FlexServ server should run in distributed mode. 0 is on single node, 1 is on multiple nodes. If not specified, it will default to 0 (single node).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--is-distributed 0"
        }
      ],
      "schedulerOptions": [
        {
          "name": "TACC Scheduler Profile",
          "description": "Scheduler profile for HPC clusters at TACC",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--tapis-profile tacc-apptainer"
        },
        {
          "name": "Slurm job name",
          "description": "Set the slurm job name to be identical to the Tapis job name.",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--job-name tap_${JobName}"
        },
        {
          "name": "TACC Resource Allocation",
          "description": "Set the TACC resource allocation for the job.",
          "inputMode": "REQUIRED",
          "arg": ""
        },
        {
          "name": "Reservation Name",
          "description": "Set the reservation name for the job.",
          "inputMode": "REQUIRED",
          "arg": ""
        }
      ],
      "envVariables": [
        {
          "key": "APPTAINER_CACHEDIR",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "value": "/work/projects/aci/cic/apps/flexserv/singularity_cache",
          "description": "Apptainer cache directory."
        },
        {
          "key": "HUGGINGFACE_TOKEN",
          "value": "hf_xxx",
          "description": "Token for accessing Hugging Face models, especially for the models that requires permission to download/use from HuggingFace. This is identical to HF_TOKEN",
          "inputMode": "INCLUDE_ON_DEMAND"
        },
        {
          "key": "FLEXSERV_TOKEN",
          "value": "flexserv",
          "description": "Optional fixed startup token. If empty, TAP token is used.",
          "inputMode": "INCLUDE_ON_DEMAND"
        },
        {
          "key": "FLEXSERV_BACKEND_TYPE",
          "value": "transformers",
          "description": "Backend type (default: transformers).",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "FLEXSERV_VENV",
          "value": "/app/venvs/flexserv",
          "description": "Venv path in container for backend/gateway startup.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "ENABLE_GATEWAY",
          "value": "true",
          "description": "Enable gateway mode (default: true).",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "GATEWAY_BACKEND_PORT",
          "value": "8001",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "description": "Gateway internal backend port."
        },
        {
          "key": "GATEWAY_PORT",
          "value": "8000",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "description": "Gateway public port. Usually matches --flexserv-port."
        },
        {
          "key": "PRI_MODEL_HOST",
          "value": "HOST_EVAL($SCRATCH)/flexserv/models",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "description": "Directory path for Private models. This applies to the $PRI_MODEL_REPO variable used in the app, it will be replaced with this path when the job is running. You can upload your private models to this directory and specify the model name (which is the subdirectory name under this directory) as the input to the app to use those models."
        },
        {
          "key": "PUB_MODEL_HOST",
          "value": "/work/projects/aci/cic/models",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "description": "Directory path for Public models. This applies to the $PUB_MODEL_REPO variable used in the app, it will be replaced with this path when the job is running. We will have some commonly used models stored in this directory for users to use, and you can also upload your models to this directory if you want to share them with other users. Similar to PRI_MODEL_HOST, you can specify the model name (which is the subdirectory name under this directory) as the input to the app to use those models."
        }
      ],
      "archiveFilter": {
        "includeLaunchFiles": true
      },
      "logConfig": {
        "stdoutFilename": "",
        "stderrFilename": ""
      }
    },
    "nodeCount": 1,
    "coresPerNode": 1,
    "memoryMB": 256000,
    "maxMinutes": 10
  },
  "tags": [
    "appName: FlexServ"
  ],
  "notes": {
    "label": "FlexServ",
    "category": "Utilities",
    "showTargetPath": true,
    "dynamicExecSystems": [
      "vista",
      "stampede3",
      "ls6"
    ]
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
