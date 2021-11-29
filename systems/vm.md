# Registering a Server
If you have access to a virtual machine (VM) or bare metal server, you can register
it as a Tapis system. To do so, you must first describe the system in a JSON object.

The following example can be modified for your VM.

``` python
system_def = {
  "id": "<userid>.<vm_hostname>",
  "description": "Tapis v3 execution system",
  "systemType": "LINUX",
  "host": "<network_address>",
  "effectiveUserId": "<system_account>",
  
  "defaultAuthnMethod": "PKI_KEYS",
  "rootDir": "/home/<system_account>",
  "canExec": True,
  "jobRuntimes": [ { "runtimeType": "DOCKER" }, { "runtimeType": "SINGULARITY" } ],
  "jobWorkingDir": "workdir",
}
```
Be sure to review the following and make any required updates:
* `<userid>.<vm_hostname>` - A unique id for this system. As indicated, we recommend using
a combination of your username and the hostname of the computer.
* `<network_address>` - The network address of the machine (e.g., an IP address or domain)
* `<system_account>` - The POSIX account on the system that Tapis should use when 
accessing the system. Note that when registering individual servers, there is often only
one POSIX account that is used, however, it is possible to support a multiple users when 
the usernames on the system match those authenticating with Tapis. In that case,
setting`effectiveUserId` to the value `"${apiUserId}` will instruct Tapis to use the API
user's identity (i.e., their username) when accessing the system.
* `/home/<system_account>` - The root directory; Tapis will prepend this path to all paths issued
against this system.
* If you want to use a password (instead of keys) to delegate authentication to Tapis, replace
`"PKI_KEYS"` with `"PASSWORD"` for the `defaultAuthnMethod`.

Note that although it is possible, we have not provided any login
credentials in the system definition. For security reasons, it is recommended that login credentials 
be updated using a separate API call as discussed below.

If your server uses SLURM to schedule jobs, you can add the following attributes to the
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

We now need to register credentials for our system so that Tapis can connect to it. We'll
register an SSH key pair that is authorized for the user we