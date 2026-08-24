# Tapis Systems

Once you are authorized to make calls to the various services, one of first things you may want to do is view storage
and execution resources available to you or create your own. In Tapis a storage or execution resource is referred
to as a **system**. Note that a single system in Tapis can act as both a storage and execution resource. It can also be
shared among users in the tenant.

## Overview
A Tapis system represents a server or collection of servers exposed through a single host name or IP address.
Each system is associated with a specific tenant. A system can be used for the following purposes:

* Running a job, including:

  * Staging files to a system in preparation for running a job.
  * Executing a job on a system.
  * Archiving files and data on a remote system after job execution.

* Storing and retrieving files and data.

Each system is of a specific type (such as LINUX or S3) and owned by a specific user who has special privileges for
the system. The system definition also includes the user that is used to access the system, referred to as
*effectiveUserId*. This access user can be a specific user (such as a service account) or dynamically specified as
``${apiUserId}``. For the case of ``${apiUserId}``, the username is extracted from the identity associated with the
request to the service.

At a high level a system represents the following information:

* **id** - A short descriptive name for the system that is unique within the tenant.
* **description** - An optional more verbose description for the system.
* **systemType** - Type of system: LINUX, S3, IRODS or GLOBUS.
* **owner** - A specific user set at system creation. By default, this is ``${apiUserId}``, the user making the request to
              create the system.
* **host** Host name or IP address.
* **effectiveUserId** - The username to use when accessing the system. A specific user (such as a service account) or the dynamic user ``${apiUserId}``
* **bucketName** For an S3 system this is the name of the bucket.
* **rootDir** - Effective root directory. Directory to be used when listing files or moving files to and from the system.
* **canExec** - Flag indicating if the system can be used to execute jobs.
* **job execution attributes** - Various attributes related to job execution such as *jobRuntimes*, *jobWorkingDir*, etc.

Note that a system may be created as a storage-only resource (*canExec=false*) or as a system that can be used for both
execution and storage (*canExec=true*).

For more information about systems and the Systems service please see [Tapis Systems Service documentation](https://tapis.readthedocs.io/en/latest/technical/systems.html).

## Getting Started

Here we review how to create a system and how to retrieve system details. In the examples below we assume you are using
the tenant named ``training`` with a base URL of ``https://training.tapis.io`` and that you have authenticated using ``tapipy``.
During the hands-on portion of the tutorial you will create two systems, one for a VM and one for an HPC cluster.

### Creating a System

Here is an example of a system definition:
``` python
system_def = {
  "id": system_id_vm,
  "description": "Test system",
  "systemType": "LINUX",
  "host": host,
  "defaultAuthnMethod": "PASSWORD",
  "rootDir": "/home/"+user_id,
  "canExec": True,
  "jobRuntimes": [ { "runtimeType": "SINGULARITY" } ],
  "jobWorkingDir": "workdir",
}
```

#### Using ``tapipy`` to register the system:
``` python
 import json
 from tapipy.tapis import Tapis
 t = Tapis(base_url='https://training.tapis.io', username='<userid>', password='************')
 t.systems.createSystem(**system_def)
```

### Registering Credentials for a System
Now that you have registered a system you will need to register credentials to allow Tapis to access the host.
Various authentication methods can be used to access a system, such as PASSWORD and PKI_KEYS. Here we will cover
registering a password.  Note that although it is possible, we have not provided any login
credentials in the system definition. For security reasons, it is recommended that login credentials be updated
using a separate API call as discussed below.

#### Using ``tapipy`` to register the credential:
``` python
 t.systems.createUserCredential(systemId=system_id_vm, userName='<userid>', password='<password>'))
```
where ``<userid>`` is replaced with your username and ``<password>`` is replaced with your password for the host.


### Viewing Systems

To retrieve details for a specific system, such as the one above:

#### Using ``tapipy``:
``` python
 t.systems.getSystem(systemId=system_id_vm)
```

## Next Steps
Now that we have covered creating and viewing a system, we are now ready to create an application that can be run on
the system (or any other system).

 [Next-> Applications](../block1/03-apps.md)
