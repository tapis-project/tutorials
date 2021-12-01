# Introduction to Tapis Apps
A Tapis application represents a piece of software that can be executed on one or more
Tapis systems producing useful results. Each application is versioned and is owned by a specific 
user who has special privileges for the application. Once an application is defined, users can
execute it on a specific system using the Jobs service. A Tapis job represents a single
execution of an app. We'll discuss jobs next, but for now, an application definition 
includes information which allows the Jobs service to:
* Stage input prior to launching the application
* Launch the application
* Monitor the application during execution
* Archive output after application execution

## Versioning
Applications are expected to evolve over time. An initial version will be created and may 
enjoy widespread use. When
the application must be modified it is important to allow for previous versions of the 
application to be used while new versions are created and tested.

The versioning scheme is at the discretion of the application author. It is 
recommended that a two or three level form of semantic versioning be used. The fully 
qualified application reference within a tenant is constructed by appending
a hyphen to the name followed by the version string. For example, the first two versions 
of an application might be *myapp-0.0.1* and *myapp-0.0.2*. If a version is not specified
when retrieving an application then by default the most recently created version of the 
application will be returned.

## Model
An application contains some information that is independent of the version and some 
information that varies by version.
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

## Next Steps
Next we'll actually look at what is involved with registering a specific application.

[Next-> Creating and Registering a Classifier App](hello.md)


## Additional Resources
For more information about applications and the Applications service 
please see [Tapis Applications Service documentation](https://tapis.readthedocs.io/en/latest/technical/apps.html).

