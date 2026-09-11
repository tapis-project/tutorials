# Materials: System and App Definitions

This tutorial runs on one Tapis system and two Tapis apps. They're already registered as public in the `public` tenant, so you don't need to create anything to follow along:

| What | Tapis ID | Where we use it |
| --- | --- | --- |
| Vista system | `vista-test-nairr` | Sections 2–4, to run jobs and browse files |
| FlexServ app | `FlexServ-1.4.0` | Section 3, to serve and chat with models |
| YOLO fine-tuning app | `yolo-finetuning-arm64` | Section 4, to fine-tune a YOLO26 model |

The definitions below are the ones we use in the tutorial, here as a quick way to copy them and create your own, for example to keep running FlexServ or fine-tuning jobs after the tutorial. Fields that Tapis fills in itself (owner, UUID, timestamps, sharing) are left out, since create requests don't accept them.

## Before You Create Them

- **Pick your own IDs.** Replace `<your-username>` in each `id`. System and app IDs must be unique in the tenant, and ours are already taken.
- **Leave the scheduler placeholders.** `<< allocation >>` and `<< reservation >>` get filled in when you submit a job, as in [Step 3.1.3](/tutorials/Tapis_FlexServ/01b-running-flexserv/#step-313-submit-flexserv-job-using-tapis-ui).
- **Add credentials after creating the system.** It signs in with TMS keys as whoever uses it (`${apiUserId}`), so press **Authenticate with TMS keys** on it, as in [Step 2.4](/tutorials/Intro_Tapis/02-initial-tapis-ui/#step-24-add-tms-credentials-for-the-nairr-vista-public-system).
- **Choose the system when you submit.** Neither app names an execution system, so pick yours, and a queue it has such as `gh-shared`, in the job launcher.

## Creating Them in TapisUI

1. **System:** in **Settings › Preferences**, set **New system dialog** to **Classic**. Then on **Systems**, press **New system**, open the JSON editor, and paste the system definition.
2. **Apps:** on **Apps**, press **New app**, choose **json editor**, and paste an app definition.

You can also send the same JSON to the Tapis API (`POST /v3/systems` and `POST /v3/apps`). The [Systems](https://tapis.readthedocs.io/en/latest/technical/systems.html) and [Apps](https://tapis.readthedocs.io/en/latest/technical/apps.html) docs describe every field.

## Definitions

<details class="accordion" markdown="1">
<summary>System: Vista (vista-test-nairr)</summary>

TACC's Vista cluster. Jobs run through Slurm with the Singularity or ZIP runtime, and each job gets its own working directory under `$SCRATCH`.

```json
{
  "id": "<your-username>-vista",
  "description": "System for running jobs on the HPC system.",
  "systemType": "LINUX",
  "host": "vista.tacc.utexas.edu",
  "effectiveUserId": "${apiUserId}",
  "defaultAuthnMethod": "TMS_KEYS",
  "rootDir": "/",
  "port": 22,
  "useProxy": false,
  "proxyPort": -1,
  "canExec": true,
  "canRunBatch": true,
  "enableCmdPrefix": true,
  "allowChildren": false,
  "jobRuntimes": [
    {
      "runtimeType": "SINGULARITY"
    },
    {
      "runtimeType": "ZIP"
    }
  ],
  "jobWorkingDir": "HOST_EVAL($SCRATCH)/tapis/${JobUUID}",
  "jobMaxJobs": 2147483647,
  "jobMaxJobsPerUser": 2147483647,
  "batchScheduler": "SLURM",
  "batchLogicalQueues": [
    {
      "name": "gg",
      "hpcQueueName": "gg",
      "maxJobs": -1,
      "maxJobsPerUser": 20,
      "minNodeCount": 1,
      "maxNodeCount": 32,
      "minCoresPerNode": 1,
      "maxCoresPerNode": 144,
      "minMemoryMB": 1,
      "maxMemoryMB": 256000,
      "minMinutes": 1,
      "maxMinutes": 2880
    },
    {
      "name": "gh-dev",
      "hpcQueueName": "gh-dev",
      "maxJobs": -1,
      "maxJobsPerUser": 2,
      "minNodeCount": 1,
      "maxNodeCount": 8,
      "minCoresPerNode": 1,
      "maxCoresPerNode": 72,
      "minMemoryMB": 1,
      "maxMemoryMB": 256000,
      "minMinutes": 1,
      "maxMinutes": 120
    },
    {
      "name": "gh",
      "hpcQueueName": "gh",
      "maxJobs": -1,
      "maxJobsPerUser": 20,
      "minNodeCount": 1,
      "maxNodeCount": 64,
      "minCoresPerNode": 1,
      "maxCoresPerNode": 72,
      "minMemoryMB": 1,
      "maxMemoryMB": 256000,
      "minMinutes": 1,
      "maxMinutes": 2880
    },
    {
      "name": "gh-shared",
      "hpcQueueName": "gh-shared",
      "maxJobs": -1,
      "maxJobsPerUser": 20,
      "minNodeCount": 1,
      "maxNodeCount": 64,
      "minCoresPerNode": 1,
      "maxCoresPerNode": 72,
      "minMemoryMB": 1,
      "maxMemoryMB": 256000,
      "minMinutes": 1,
      "maxMinutes": 2880
    }
  ],
  "batchDefaultLogicalQueue": "gh",
  "batchSchedulerProfile": "tacc-apptainer",
  "notes": {
    "label": "Vista"
  }
}
```

</details>

<details class="accordion" markdown="1">
<summary>App: FlexServ (FlexServ-1.4.0)</summary>

Starts a FlexServ inference server on a compute node from the FlexServ release ZIP. In Section 3 we use it to load models and chat with them.

```json
{
  "id": "<your-username>-flexserv",
  "version": "1.4.0",
  "description": "A TACC-owned inference server for running AI models.",
  "runtime": "ZIP",
  "runtimeOptions": [
    "SINGULARITY_RUN"
  ],
  "containerImage": "https://github.com/tapis-project/FlexServ-Deployer/releases/download/tapis-flexserv-1.4.0/Tapis-FlexServ.zip",
  "jobType": "BATCH",
  "maxJobs": 2147483647,
  "maxJobsPerUser": 2147483647,
  "strictFileInputs": true,
  "jobAttributes": {
    "description": "FlexServ run by ${JobOwner}",
    "dynamicExecSystem": false,
    "execSystemExecDir": "${JobWorkingDir}",
    "execSystemInputDir": "${JobWorkingDir}",
    "execSystemOutputDir": "${JobWorkingDir}/output",
    "execSystemLogicalQueue": "debug",
    "archiveSystemDir": "HOST_EVAL($WORK)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}",
    "archiveOnAppError": false,
    "isMpi": false,
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
          "name": "trustRemoteCode",
          "description": "Whether to trust remote code execution (default: false).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--trust-remote-code false"
        },
        {
          "name": "continuousBatching",
          "description": "Whether to enable continuous batching (default: false).",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "--continuous-batching false"
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
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "-A << allocation >>"
        },
        {
          "name": "Reservation Name",
          "description": "Set the reservation name for the job.",
          "inputMode": "INCLUDE_ON_DEMAND",
          "arg": "--reservation << reservation >>"
        }
      ],
      "envVariables": [
        {
          "key": "APPTAINER_CACHEDIR",
          "value": "/work/projects/aci/cic/apps/flexserv/singularity_cache",
          "description": "Apptainer cache directory.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "HUGGINGFACE_TOKEN",
          "value": "hf_xxx",
          "description": "Token for accessing Hugging Face models, especially for the models that requires permission to download/use from HuggingFace. This is identical to HF_TOKEN",
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
          "description": "Gateway internal backend port.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "GATEWAY_PORT",
          "value": "8000",
          "description": "Gateway public port. Usually matches --flexserv-port.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "PRI_MODEL_HOST",
          "value": "HOST_EVAL($SCRATCH)/flexserv/models",
          "description": "Directory path for Private models. This applies to the $PRI_MODEL_REPO variable used in the app, it will be replaced with this path when the job is running. You can upload your private models to this directory and specify the model name (which is the subdirectory name under this directory) as the input to the app to use those models.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "PUB_MODEL_HOST",
          "value": "/work/projects/aci/cic/models",
          "description": "Directory path for Public models. This applies to the $PUB_MODEL_REPO variable used in the app, it will be replaced with this path when the job is running. We will have some commonly used models stored in this directory for users to use, and you can also upload your models to this directory if you want to share them with other users. Similar to PRI_MODEL_HOST, you can specify the model name (which is the subdirectory name under this directory) as the input to the app to use those models.",
          "inputMode": "INCLUDE_BY_DEFAULT"
        }
      ],
      "archiveFilter": {
        "includeLaunchFiles": true
      }
    },
    "nodeCount": 1,
    "coresPerNode": 16,
    "memoryMB": 256000,
    "maxMinutes": 240
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
    ],
    "hideNodeCountAndCoresPerNode": false
  }
}
```

</details>

<details class="accordion" markdown="1">
<summary>App: YOLO fine-tuning (yolo-finetuning-arm64)</summary>

Fine-tunes an Ultralytics YOLO26 model on a GPU node using the tutorial's Singularity image. In Section 4 we use it to fine-tune the detection model.

```json
{
  "id": "<your-username>-yolo-finetuning",
  "version": "1.2",
  "description": "An app to fine-tune ultralytics Yolo26 model using Singularity in batch mode.",
  "runtime": "SINGULARITY",
  "runtimeOptions": [
    "SINGULARITY_RUN"
  ],
  "containerImage": "/work/projects/aci/cic/apps/yolo_finetune/finetune_arm64_latest.sif",
  "jobType": "BATCH",
  "maxJobs": 2147483647,
  "maxJobsPerUser": 2147483647,
  "strictFileInputs": false,
  "jobAttributes": {
    "dynamicExecSystem": false,
    "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
    "execSystemInputDir": "${JobWorkingDir}/jobs/${JobUUID}/data",
    "execSystemOutputDir": "${JobWorkingDir}/jobs/${JobUUID}/ultralytics",
    "archiveSystemDir": "HOST_EVAL($WORK)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}",
    "archiveOnAppError": false,
    "isMpi": false,
    "parameterSet": {
      "containerArgs": [
        {
          "name": "nvidia",
          "inputMode": "FIXED",
          "arg": "--nv"
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
          "name": "TACC Resource Allocation",
          "description": "Set the TACC resource allocation for the job.",
          "inputMode": "INCLUDE_BY_DEFAULT",
          "arg": "-A << allocation >>"
        },
        {
          "name": "Reservation Name",
          "description": "Set the reservation name for the job.",
          "inputMode": "INCLUDE_ON_DEMAND",
          "arg": "--reservation << reservation >>"
        }
      ],
      "envVariables": [
        {
          "key": "EPOCHS",
          "value": "10",
          "description": "Number of epochs for the fine-tune job",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "YOLO_26_MODEL",
          "value": "yolo26l",
          "description": "YOLO26 model to fine-tune, e.g. yolo26n or yolo26l",
          "inputMode": "INCLUDE_BY_DEFAULT"
        },
        {
          "key": "TWO_STAGE_FINE_TUNE",
          "value": "true",
          "description": "Whether to use two-stage fine-tuning",
          "inputMode": "INCLUDE_ON_DEMAND"
        },
        {
          "key": "FREEZE",
          "value": "10",
          "description": "Number of layers to freeze during the first stage",
          "inputMode": "INCLUDE_BY_DEFAULT"
        }
      ],
      "archiveFilter": {
        "includeLaunchFiles": false
      }
    },
    "nodeCount": 1,
    "coresPerNode": 16,
    "memoryMB": 96000,
    "maxMinutes": 120
  }
}
```

</details>
