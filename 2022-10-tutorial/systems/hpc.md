# Registering an HPC System
HPC systems usually rely on a batch scheduler such as Slurm to schedule jobs on a cluster
of machines. You can register an HPC cluster as a Tapis system to enable to Tapis to 
submit and monitor jobs on the cluster for you.

In this example, we will register system on the Stampede2 supercomputer at TACC. Access to
Stampede2 requires that your TACC account have a valid allocation on 
Stampede2. If you do not have an allocation on Stampede2, you can still use the concepts
illustrated in this tutorial to register another HPC cluster that you do have access to.

## The System Description 
To register a system with Tapis, you describe the system in a JSON object. The description
includes information about how to connect to the system, what kind of conatiner runtimes
are available, what scheduler types, the queues defined, and more.

The following contains a description of the Stampede2 cluster. Copy and paste the code
below into your Jupyter notebook, and update `<username>` in the `id` field to your
Tapis username.

```python
s2_system = {
  "id": "stampede2.<username>",
  "description": "System for running jobs on the Stampede2 cluster",
  "systemType": "LINUX",
  "host": "stampede2.tacc.utexas.edu",
  "defaultAuthnMethod": "PKI_KEYS",
  "effectiveUserId": "${apiUserId}",
  "port": 22,
  "rootDir": "/",
  "canExec": True,
  "jobRuntimes": [ { "runtimeType": "SINGULARITY" } ],
  "jobWorkingDir": "HOST_EVAL($WORK2)",
  "canRunBatch": True,
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
In the description above, we set `effectiveUserId` to the string `${apiUserId}`. Recall that
this tells Tapis to use the identity (that is, the `username`) associated with the token on
the API request whenever it interacts with this system. We could have just hard-coded our
own username (e.g., `"jstubbs"`) instead, but this approach means that if we share the 
system with another Tapis user, Tapis will use that user's identity to interact with the
system instead of our own. We'll cover sharing in more detail in a future tutorial.

To keep things simple, our description of Stampede2 includes just one queue, the normal 
queue. We can add additional queues to the description if we wish to submit jobs to them.

Note also our use of `HOST_EVAL($WORK2)` for `jobWorkingDir`. The `HOST_EVAL()` function
instructs Tapis to evaluate an environment variable (in this case, the `$WORK2` variable)
_on the host itself_ to determine the working directory for jobs. This is useful 
whenever you want the job working directory to be dynamically determined from a variable
defined on the system.

With the system description defined, we are ready to register it with Tapis. We do that
as follows:

```python
t.systems.createSystem(**s2_system)
```

We should now be able to list systems and see our Stampede2 system

```python
t.systems.getSystems()
```

The output should include something like this:
```python
[
 canExec: true
 defaultAuthnMethod: PKI_KEYS
 effectiveUserId: jstubbs
 host: stampede2.tacc.utexas.edu
 id: stampede2.jstubbs
 owner: jstubbs
 systemType: LINUX,
 ...
]
```

We can also retrieve full details about our system using its id (update the `<username>`
in the call below):

```python
t.systems.getSystem(systemId='stampede2.<username>')
```

The output is much more verbose:

```python
authnCredential: None
batchDefaultLogicalQueue: tapisNormal
batchLogicalQueues: [
hpcQueueName: normal
maxCoresPerNode: 68
maxJobs: 50
maxJobsPerUser: 10
maxMemoryMB: 16384
maxMinutes: 60
maxNodeCount: 16
minCoresPerNode: 1
minMemoryMB: 1
minMinutes: 1
minNodeCount: 1
name: tapisNormal]
...
```

## Next Steps
Note that before we can actually use this system with Tapis, we will need to register
at least one credential for it. We will do that next.

[Next-> Registering System Credentials](credentials.md)


## Additional Resources
* _Additional details about the Systems endpoints_ - API [specification](https://tapis-project.github.io/live-docs/?service=Systems)