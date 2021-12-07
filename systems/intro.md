# Introduction to Tapis Systems
Once you are authorized to make calls to the various services, one of first things you may 
want to do is view storage
and execution resources available to you or create your own. In Tapis, a storage or 
execution resource is referred
to as a **system**. Note that a single system in Tapis can act as both a storage and 
execution resource. It can also be shared among Tapis users.

## Overview
A Tapis system represents a server or collection of servers exposed through a single host name or IP address.
A system can be used for the following purposes:

* Running a job, including:

  * Staging files to a system in preparation for running a job.
  * Executing a job on a system.
  * Archiving files and data on a remote system after job execution.

* Storing and retrieving files and data.

Each system is of a specific type (such as `LINUX` or `S3`) and owned by a specific user 
who has special privileges for
the system. The system definition also includes the user that is used to access the system, 
referred to as
*effectiveUserId*. This access user can be a specific user (such as a service account) or dynamically specified as
``${apiUserId}``. For the case of ``${apiUserId}``, the username is extracted from the identity associated with the
request to the service.

At a high level a system represents the following information:

* **id** - A short descriptive name for the system that is unique within the tenant.
* **description** - An optional more verbose description for the system.
* **systemType** - Type of system: LINUX, S3. Support for  IRODS and GLOBUS is under development.
* **owner** - A specific user set at system creation. By default, this is ``${apiUserId}``, the user making the request to
              create the system.
* **host** Host name or IP address.
* **effectiveUserId** - The username to use when accessing the system. A specific user (such as a service account) or the dynamic user ``${apiUserId}``
* **bucketName** For an S3 system this is the name of the bucket.
* **rootDir** - Effective root directory. Directory to be used when listing files or moving files to and from the system.
* **canExec** - Flag indicating if the system can be used to execute jobs.
* **job execution attributes** - Various attributes related to job execution such as *jobRuntimes*, *jobWorkingDir*, etc.

Note that a system may be created as a storage-only resource (`canExec=false`) or as a system that can be used for both
execution and storage (`canExec=True`).

## First API Calls With the Systems Service
As with other Tapis services, using `tapipy` to make API calls to the Systems service will 
use take the form `t.systems.<endpoint>(args)` for some `<endpoint>`.  

For example, we can get a list of all the systems we have access to using:
```python
t.systems.getSystems()
```
The response will show us a summary of each system. If we want full details about a 
specific system, we can use

```python
 t.systems.getSystem(systemId='some_system_id')
```
Note that you will not have access to any systems until you have registered some. We will
do that in the next tutorial.

## Next Steps
Now that we have covered the concept of Tapis systems, let's begin by registering 
an HPC system. If you do not have access to an HPC system, you might be interested in 
registering another kind of system, such as a server or an S3 bucket. See the list
of **All Tapis Systems Tutorials** from the [home page](https://tapis-project.github.io/tutorials/).


 [Next-> Registering an HPC System](hpc.md)


## Additional Resources 
* _Additional information about Systems_ - Reference [documentation](https://tapis.readthedocs.io/en/latest/technical/systems.html).