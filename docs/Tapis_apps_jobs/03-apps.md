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
* **runtime** - Runtime to be used when executing the application. DOCKER, SINGULARITY. Default is DOCKER.
* **containerImage** - Reference to be used when running the container image.
* **maxJobs** - Maximum total number of jobs that can be queued or running for this application on a given execution  
  system at a given time. Note that the execution system may also limit the number of jobs on the system which may
  further restrict the total number of jobs. Set to -1 for unlimited. Default is unlimited.
* **maxJobsPerUser** - Maximum total number of jobs associated with a specific job owner that can be queued or running for
  this application on a given execution system at a given time. Note that the execution system may also limit the number
  of jobs on the system which may further restrict the total number of jobs. Set to -1 for unlimited. Default is unlimited.
* **strictFileInputs** -  Flag indicating if a job request is allowed to have unnamed file inputs. If set to true then a
  job request may only use the named file inputs defined in the application. See attribute *fileInputs* in the
  JobAttributes table. Default is *false*.
* **Job related attributes** - Various attributes related to job execution such as *execSystemId*, *execSystemExecDir*,
  *execSystemInputDir*, *execSystemLogicalQueue* *archiveSystemId*, *fileInputs*, etc. Many of these are optional.

For more information about applications and the Applications service please see [Tapis Applications Service documentation](https://tapis.readthedocs.io/en/latest/technical/apps.html).

## Getting Started

Here we review how to create an application and how to retrieve application details. In the examples below we assume you are using the tenant named ``training`` with a base URL of ``https://training.tacc.tapis.io`` and that you have authenticated using ``tapipy``.

### Creating an Application

Here is an example of an application definition:
``` python
app_def = {
    "id": app_id,
    "version": "0.2",
    "description": "Application utilizing the sentiment analysis model from Hugging Face.",
    "jobType": "FORK",
    "runtime": "DOCKER",
    "containerImage": "tapis/sentiment-analysis:1.0.0",
    "jobAttributes": {
        "parameterSet": {
            "archiveFilter": {
                "includeLaunchFiles": False
            }
        },
        "memoryMB": 1,
        "nodeCount": 1,
        "coresPerNode": 1,
        "maxMinutes": 10
    }
}
```

#### Using ``tapipy`` to register the application:
``` python
 import json
 from tapipy.tapis import Tapis
 t = Tapis(base_url='https://training.tapis.io', username='<userid>', password='************')
 t.apps.createAppVersion(**app_def)
```

### Viewing Applications

To retrieve details for a specific application, such as the one above:

#### Using ``tapipy``:
``` python
 t.apps.getAppLatestVersion(appId=app_id)
```

## Next Steps
Now that we have our very first application ready to use, we are ready to run it on a system using the Jobs service. 

[Next-> Jobs](./04-jobs.md)
