# Hands-on TapisUI Exercises

Login to https://training.tapis.io. Use the username and password provided to you to authenticate.

<img src="/tutorials/assets/demo/login-tapis.png" style="max-width:60%;">

## Systems

In this section, we will create two Tapis systems: one for running jobs on a VM host using FORK, and another for running jobs on an HPC-type host using BATCH.


{: .note}
> ⚠️ Note: While it is possible to include login credentials in the system definitions, we have not done so here. Well-crafted system definitions are often copied and reused. For security reasons, it is recommended to register login credentials separately.

When you log in to Tapis UI, you may see My Systems showing "0", as no systems have been created yet. As you create systems, this list will populate accordingly. However, you should still see some public systems already available.

### Create System

Click on Systems from the left-hand menu, then click the Create System button in the top-right corner. You will see two options for creating a system:

- By filling out a form, or 
- Using the JSON Editor

For this tutorial, we will use the JSON Editor.

<img src="/tutorials/assets/demo/create-system.png" style="max-width:80%;">

Copy the system JSON provided below into the editor, then click Create System.

```json
{
  "id": "pearc25-vm-system-training",
  "description": "Test system",
  "systemType": "LINUX",
  "host": "129.114.35.138",
  "effectiveUserId":"${apiUserId}",
  "defaultAuthnMethod": "PASSWORD",
  "rootDir": "/",
  "canExec": true,
  "jobRuntimes": [ { "runtimeType": "DOCKER" } ],
  "jobWorkingDir": "HOST_EVAL($HOME)/sharetest/workdir"
}
```

In the My Systems you should now see the system you just created.

### Register Credentials for the VM system

After creating the system, you will need to register credentials for your username. These credentials allow Tapis to access the host system on your behalf.

Tapis supports various authentication methods, such as PASSWORD and PKI_KEYS. In this tutorial, we will show you how to add password-based credentials for your system.

You will need to use the provided vm_password for this step.

<img src="/tutorials/assets/demo/authenticate-system.png" style="max-width:80%;">

Click on the AUTHENTICATE and add Password

<img src="/tutorials/assets/demo/add-password-system.png" style="max-width:80%;">

You should see Successfully created credentials. If there is any error please try to enter the vm_password again

<img src="/tutorials/assets/demo/credentials-success.png" style="max-width:80%;">

Now that you have successfully added your credentials, your system is ready to use.

To verify this, go to the Files tab from the left-hand menu and try listing the files.
You should see something similar to the image below.

<img src="/tutorials/assets/demo/files-list-vm.png" style="max-width:92%;">

We will now learn to create a Sentiment Analysis Application with Tapis.

## Natural Language Processing: Sentiment Analysis

- Sentiment Analysis is one of the most popular applications of Natural Language Processing, which uses the Text Classification method to analyse the sentiment or emotion of the given text.
- Sentiment analysis assigns a label like 🙂 positive, 🙁 negative, or 😐 neutral to a sequence of text.
- It is useful tool to make business decisions based on customer feedback and reviews.

### Understanding the Sentiment Analysis Model

This tutorial uses the Hugging Face transformers library for sentiment analysis. Here's a quick example of how the model works (installed with "pip install -q transformers"):

```python
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

text = "Glad to see you at PEARC 25"
sentiment_pipeline(text)
```

This would return a result indicating positive sentiment with a confidence score.

TODO TODO TODO - ADD RESULT CODE BLOCK

### Create App with TapisUI

We'll be creating an App with TapisUI now. Create an app by navigating to the Apps Tab in TapisUI and click on "+ NEW APP" at the top right.
<img src="/tutorials/assets/demo/create-app-button.png" style="max-width:80%;">

Once we have the app creation modal, we want to switch to "JSON EDITOR" and paste in our VM configuration.

<img src="/tutorials/assets/demo/create-app-vm.png" style="max-width:80%;">

The following is our app definition:

```json
{
    "id": "pearc25-sentiment-analysis-app-vm",
    "version": "0.1",
    "description": "Application utilizing the sentiment analysis model from Hugging Face.",
    "jobType": "FORK",
    "runtime": "DOCKER",
    "containerImage": "tapis/sentiment-analysis:2.0.2",
    "jobAttributes": {
        "parameterSet": {
            "archiveFilter": {
                "includeLaunchFiles": false
            }
        },
        "memoryMB": 1,
        "nodeCount": 1,
        "coresPerNode": 1,
        "maxMinutes": 10
    }
}
```

Click on Create App and it should give a success message.

## Submit Job in Tapis UI

In the Apps Tab, click on the Application you created. You should see Submit job button, click that and enter the below job json in the JSON EDITOR, and click submit.

<img src="/tutorials/assets/demo/submitjobjson.png" style="max-width:80%;">

```json
{
    "name":"sentiment analysis",
    "description":"sentiment analysis with hugging face transformer pipelines",
    "appId":"pearc25-sentiment-analysis-app-vm",
    "appVersion":"0.1",
    "execSystemId":"pearc25-vm-system-training", 
    "parameterSet": {
    "appArgs": [
            {"arg": "--sentences"},
            {"arg": "\"This is great\" \"This is not fun\""},
            {"arg": "--output-filepath"},
            {"arg":"/TapisOutput/results.csv"}
            
        ]
    }
}
```

Once the job successfully finishes you should see a results.csv file which has the results from sentiment analysis on the sentences provided in the job

<img src="/tutorials/assets/demo/job-vm-success.png" style="max-width:80%;">

## Running on HPC Systems

### Create a system for the HPC cluster

With just a few changes to the system definition you can create a second system that can be used to run the same application on an HPC type host. Note the minimal changes:

* **id** - A unique id is required
* **host** - Main hostname for the HPC system.
* **rootDir** - Using the root directory of the host gives us flexibility in setting **jobWorkingDir**. Note that you still need LINUX permissions.
* **jobWorkingDir** - Now determined dynamically using the Tapis v3 function HOST_EVAL()
* **jobRuntimes** - Most HPC systems support singularity and not docker
* **batchLogicalQueue.hpcQueueName** - HPC queue to use by default.
* **batchLogicalQueues** - HPC queue definitions for this HPC system.

In the Tapis UI, Systems Tab. Click on + CREATE SYSTEM, copy the below json in JSON EDITOR and click CREATE SYSTEM.

```json
{
  "id": "pearc25-system-id-hpc",
  "description": "System for testing jobs on an HPC type host for PEARC25",
  "systemType": "LINUX",
  "host": "129.114.35.138",
  "defaultAuthnMethod": "PASSWORD",
  "effectiveUserId": "${apiUserId}",
  "rootDir": "/",
  "canExec": true,
  "jobRuntimes": [ { "runtimeType": "SINGULARITY" } ],
  "jobWorkingDir": "HOST_EVAL($HOME)/sharetest/workdir",
  "canRunBatch": true,
  "batchScheduler": "SLURM",
  "batchSchedulerProfile": "tacc",
  "batchDefaultLogicalQueue": "tapisNormal",
  "batchLogicalQueues": [
    {
      "name": "tapisNormal",
      "hpcQueueName": "normal",
      "maxJobs": 50,
      "maxJobsPerUser": 10,
      "minNodeCount": 1,
      "maxNodeCount": 16,
      "minCoresPerNode": 1,
      "maxCoresPerNode": 68,
      "minMemoryMB": 1,
      "maxMemoryMB": 16384,
      "minMinutes": 1,
      "maxMinutes": 60
    }
  ]
}
```

Once the HPC System is successfully created it should show up in My Systems.

### Register Credentials for the HPC system

As before, now you will need to register credentials for your username. Use the "vm_password" to add credentials.

Once you get a message that system credentials were successfully created, you should be able to list files on that system.
Go to the files tab and click on the system-id that was created recently.

<img src="/tutorials/assets/demo/files-list-hpc.png" style="max-width:92%;">

## Create HPC Application

In order to run a job on a system you will need to create a Tapis application that can be run on the VM host or the HPC cluster.

<img src="/tutorials/assets/demo/create-app-hpc.png" style="max-width:80%;">

Copy the json in JSON EDITOR + NEW APP

```json
{
    "id": "pearc25-sentiment-analysis-app-hpc-training",
    "version": "0.1",
    "description": "Application utilizing the sentiment analysis model from Hugging Face.",
    "jobType": "BATCH",
    "runtime": "SINGULARITY",
    "runtimeOptions": ["SINGULARITY_RUN"],
    "containerImage": "/tmp/sentiment-analysis_2.0.2.sif",
    "jobAttributes": {
            "parameterSet": {
            "archiveFilter": {
                "includeLaunchFiles": false
            }
        },
        "memoryMB": 1,
        "nodeCount": 1,
        "coresPerNode": 1,
        "maxMinutes": 10
    }
}
```

### Submit Job on HPC

```json
{
    "name":"sentiment analysis hpc",
    "description":"sentiment analysis with hugging face transformer pipelines",
    "appId":"pearc25-sentiment-analysis-app-hpc-training",
    "appVersion":"0.1",
    "execSystemId":"pearc25-system-id-hpc", 
    "parameterSet": {
    "appArgs": [
            {"arg": "--sentences"},
            {"arg": "\"This is great\" \"This is not fun\""},
            {"arg": "--output-filepath"},
            {"arg":"./output/results.csv"}
            
        ]
    }
}
```

### Setting Notifications on Job Events

Note: Make sure to add your email address in the submitJob call.

```json
{
    "name":"sentiment analysis hpc",
    "description":"sentiment analysis with hugging face transformer pipelines",
    "appId":"pearc25-sentiment-analysis-app-hpc-training",
    "appVersion":"0.1",
    "execSystemId":"pearc25-system-id-hpc", 
    "parameterSet": {
    "appArgs": [
            {"arg": "--sentences"},
            {"arg": "\"This is great\" \"This is not fun\""},
            {"arg": "--output-filepath"},
            {"arg":"./output/results.csv"}
            
        ]
    },
    "subscriptions": 
    [ 
      { 
        "description": "Test subscriptions", 
        "eventCategoryFilter": "ALL",
        "deliveryTargets": [ { "deliveryMethod": "EMAIL","deliveryAddress":"***"}]
      }
    ]
}
```

### Cancel/Resubmit a Job

You may cancel a job if it is not in the terminating state by clicking the CANCEL JOB button in Tapis UI. Similarly you can resubmit a job by clicking the RESUBMIT button.

### App Share/Unshare

Apps can be shared or unshared with other users from TapisUI.
