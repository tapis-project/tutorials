# Executing the Classifier App
In this tutorial, we will execute our classifier application on Stampede2. If you haven't
already, you might want to work through these tutorials first:
* [Creating an HPC System](../systems/hpc.md)
* [Creating and Registering a Classifier app](../apps/hello.md)

To execute our classifier application on a system, we submit a _job_ to the Tapis Jobs
service, passing any required and optional arguments controlling how the application is
launched. When we submit a job request, the Jobs service first validates the request
(for example, that the application and system exist, that we are authorized to execute
the application on the system, etc.). If validation is successful, the Jobs service 
generates a `jobId` for our job and returns a response.

## Submitting the Job
First, we describe the job we want to execute. Enter the following into a Jupyter notebook cell:
```python
input_url = 'https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231410/Labrador-Retriever-On-White-01.jpg'
job = {
    "name": "test_job",
    "appId": "img-classify.jstubbs", 
    "appVersion": "0.1.0",
    "parameterSet": {"appArgs": [{"name": "arg1", 
                                  "arg": input_url}]        
                    }
}
```
If you have multiple allocations on Stampede2 you will also need to specify the project to 
use for the job. You can do that with:
```python
some_project = 'MY_TACC_PROJECT'
job["schedulerOptions"] = [{"arg": f"--account {some_project}"}]
```
We can now submit the job with:
```python

job = t.jobs.submitJob(**job)
job
```
If successful, the `job` object should look something like.
```
containerImage: docker://tapis/img-classify:0.1.0
created: 2021-12-01T18:41:11.233662Z
deleted: False
description: Simple image classifier demo application
enabled: True
id: img-classify.jstubbs
jobAttributes: 
archiveOnAppError: False
archiveSystemDir: None
archiveSystemId: None
coresPerNode: 1
description: None
dynamicExecSystem: False
execSystemConstraints: None
execSystemExecDir: None
execSystemId: stampede2.jstubbs
execSystemInputDir: None
execSystemLogicalQueue: None
execSystemOutputDir: None
fileInputArrays: []
fileInputs: []
maxMinutes: 10
memoryMB: 100
nodeCount: 1
parameterSet: 
appArgs: [
arg: --image_file
description: None
inputMode: INCLUDE_ON_DEMAND
name: arg1]
archiveFilter: 
excludes: []
includeLaunchFiles: False
includes: []
containerArgs: []
envVariables: []
schedulerOptions: []
subscriptions: []
tags: []
jobType: BATCH
maxJobs: 0
maxJobsPerUser: 0
notes: 

owner: jstubbs
runtime: SINGULARITY
runtimeOptions: ['SINGULARITY_RUN']
runtimeVersion: None
strictFileInputs: False
tags: []
tenant: tacc
updated: 2021-12-01T18:41:11.233662Z
uuid: 153b69ab-29db-47e7-8453-03c15b9cb8b3
version: 0.1.0
```

In particular, it is worth noting the `uuid` attribute of the job 
(`153b69ab-29db-47e7-8453-03c15b9cb8b3` in the above example), 
since we will use this
to check the status of our job:
```python
job_id = job.uuid
```

##  Get the Job Status
We can use `job_id` to check on the job's status:
```
t.jobs.getJobStatus(jobUuid=job_id)
```
You should see
```
status: <some status>
```

### Download job output
Once the job has completed and reached a status of `FINISHED`, we can download the
job output:

```
# Download output of the job
print("Job Output file:")

print("****************************************************")
jobs_output= t.jobs.getJobOutputDownload(jobUuid=job_id, outputPath='tapisjob.out')
print(jobs_output_hpc)
print("****************************************************")
```


### Analyzing Jobs Output
With the code below, you can extract the image classifier output, which returns 5 
prediction scores:

```
print ("==============Image Classifier Scores ============================")
s = jobs_output.split(b'\n')
s.reverse()
scores=[]
for i in range(1,6):
    scores.append(s[i])
    print (s[i])
```

You should see the result as below:

```
==============Image Classifier Scores ============================
b'Saint Bernard, St Bernard (score = 0.00067)'
b'bull mastiff (score = 0.00095)'
b'kuvasz (score = 0.00099)'
b'golden retriever (score = 0.00324)'
b'Labrador retriever (score = 0.97471)'
```

That's it! You have executed a job on the Stampede2 supercomputer using Tapis and
downloaded and analyzed the output.