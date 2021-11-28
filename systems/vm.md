# Creating a VM System
If you have access to a cloud virtual machine (VM) or bare metal server, you can register
it as a Tapis system. To do so, you must first describe the system in a JSON object.

The following example can be modified for your VM.

``` python
system_def = {
  "id": "<userid>.<vm_hostname>",
  "description": "Tapis v3 execution system",
  "systemType": "LINUX",
  "host": "<network_address>",
  "effectiveUserId": "${apiUserId}",
  "defaultAuthnMethod": "PASSWORD",
  "rootDir": "/home/<userid>",
  "canExec": True,
  "jobRuntimes": [ { "runtimeType": "DOCKER" }, { "runtimeType": "SINGULARITY" } ],
  "jobWorkingDir": "workdir",
}
```
Be sure to replace the following:
* `<userid>.<vm_hostname>` - A unique id for this system. As indicated, we recommend using
a combination of your username and the hostname of the computer.
* `<network_address>` - The network address of the machine (e.g., an IP address or domain)
* `/home/<userid>` - The root directory; Tapis will prepend this path to all paths issued
against this system.
* 

Note that although it is possible, we have not provided any login
credentials in the system definition. For security reasons, it is recommended that login credentials be updated
using a separate API call as discussed below.


If your VM uses SLURM to schedule jobs, you can add the following attributes to the
system definition:
```python
{
  "jobIsBatch": True,
  "batchScheduler": "SLURM",
  "batchSchedulerProfile": "tacc",
  "batchLogicalQueues": [
    {
      "name": "tapisNormal",
      "hpcQueueName": "debug",
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
  ],
  "batchDefaultLogicalQueue": "tapisNormal",
}
```