# Creating and Registering a Classifier App

In this tutorial, we cover how to create an application and how to retrieve application 
details. As a starting point for this tutorial, we have some software that has been 
containerized using Docker.

We're using a simple image classifier application to illustrate the concepts. Our image
classifier takes a single image file as an input, and it attempts to classify the objects
in the image. The source code for our image classifier can be found on GitHub
[here](https://github.com/tapis-project/application-repository/tree/main/img-classify).

## Container Runtime for the Application
When creating an application for Tapis, one should consider the types of systems where
the application should run. Tapis strives to enable you to create _portable_ applications,
that is, applications you can easily run on different machines. A major consideration
in this regard is the container runtime used to package and execute the application.

Different execution systems support different container runtimes; for example, many 
VMs and high-throughput cloud Linux servers come with support for running Docker 
containers. HPC systems tend to support Singularity but not Docker due to the security
issues running Docker in a multi-user environment. The choice of container runtime used
to package the application will impact which systems the application can run on.

Tapis supports applications packaged with either Docker or Singularity applications, but 
the semantics of invoking the application differ significantly between the two runtimes.
Therefore, It is important to decide which container runtime you will use to package 
your application because it will impact how you register it with Tapis and what
systems you can execute it on.

## Building the Application Container Image
In this tutorial, we will use Singularity for our application container runtime because 
Singularity is the only container runtime available on many HPC systems, including 
Stampede2. 

The first step is to build a Singularity image for our application. In fact, what we will 
actually do is build a _Docker_ image for our application and then convert it to 
Singularity. We'll even instruct Tapis to do the conversion to Singularity for us.

So we begin now by building a Docker image for our application. A complete discussion
of writing a Dockerfile for building a Docker image is beyond the scope of this tutorial. 
For our purposes, we'll assume we have the Dockerfile written (the repository above
includes one).

If we clone the [repository](https://github.com/tapis-project/application-repository.git) and change into the `img-classify/docker_build` directory,
we can build a Docker image with the following command:

```
docker build -t tapis/img-classify:0.1 .
```

Note that the `tapis` organization in the image name (`tapis/img-classify`) above is 
restricted to Tapis administrators. You should use your personal account or a different 
organization that you have access to. 

## Testing the Application Container Locally
We can test our image by executing a container locally, passing a URL to a file as the
input via the `--image_file` flag.

Run the following command in your shell: 
```
docker run tapis/img-classify:0.1 --image_file=https://s3.amazonaws.com/cdn-origin-etr.akc.org/wp-content/uploads/2017/11/12231410/Labrador-Retriever-On-White-01.jpg
```
You should see output similar to the following
```
>> Downloading inception-2015-12-05.tgz 100.0%2021-11-30 20:42:40.543476: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2021-11-30 20:42:41.060246: W tensorflow/core/framework/op_def_util.cc:343] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
...
Successfully downloaded inception-2015-12-05.tgz 88931400 bytes.
Labrador retriever (score = 0.97471)
golden retriever (score = 0.00324)
kuvasz (score = 0.00099)
bull mastiff (score = 0.00095)
Saint Bernard, St Bernard (score = 0.00067)
```
The output says our image classifier application classified the image as a labrador
retriever with 97.4% certainty. Looks like it is working pretty well!

## Publishing the Image to a Public Image Registry
The command above created a Docker image on our local machine. In order for Tapis to make
use of it, we need to publish the image to a Docker registry. The Docker 
[Hub](https://hub.docker.com) is a popular registry with millions of images, but Tapis 
can utilize other Docker image registries so long as the image is publicly available.

For this tutorial, we'll publish the image to Docker Hub. We can do that with the 
following command:

```
docker push tapis/img-classify:0.1
```
Note that in order to push your image to Docker Hub, you must have an account and login 
with the `docker login` command. Additionally, you must have publish writes for the 
organization where you are trying to publish the image.

## Creating an Application Definition
Now that the container image is created and published to Docker Hub, we are ready to 
create a Tapis app description of it. Recall that we are planning to register this
application as a Singularity application. We'll instruct Tapis to convert the Docker
image to Singularity for us.

Here is an example of an application definition:
``` python
app_def = {
  "id": "img-classify.<userid>",
  "version": "0.1.0",
  "description": "Simple image classifier demo application",
  "runtime": "SINGULARITY",
  "runtimeOptions": ["SINGULARITY_RUN"],
  "containerImage": "docker://tapis/img-classify:0.1.0",
  "jobType": "BATCH",
  "jobAttributes": {
    "parameterSet": {
      "appArgs": [ {"name": "arg1", "arg": "--image_file", "inputMode": "FIXED"}
      ],
      "archiveFilter": { "includeLaunchFiles": False }
    },
    "execSystemId": "stampede2.<userid>",
    "nodeCount": 1,
    "coresPerNode": 1,
    "memoryMB": 1,
    "maxMinutes": 10
  }
}
```
Note:
* You should replace both instances of ``<userid>`` with your username.
* Specifying `"runtimeOptions": ["SINGULARITY_RUN"]` instructs Tapis to use the 
`singularity run` command to execute the container. Tapis also supports executing 
Singularity containers with the `singualrity instance start` command. More details
can be found in the Jobs [documentation](https://tapis.readthedocs.io/en/latest/technical/jobs.html#singularity).
* By specifying `containerImage` as `docker://tapis/img-classify:0.1.0`, Tapis will 
pull the `tapis/img-classify:0.1.0` image from Docker Hub and convert it to a 
Singularity image.
* If we have a Singularity image file, we could have used `/path/to/my_sing_img.sif` as
the value for `containerImage` instead. 
* Specifying `"jobType": "BATCH"` and `"executionSystem": "stampede2.<userid>"` should
be thought of as the _defaults_ for the application; they can be overriden when
submitting the job.

We can now register the app with Tapis using the following:

```python
t.apps.createAppVersion(**app_def)
```

We should now be able to retrieve a description of the application we just registered:

```python
t.apps.getApp(appId='img-classify.jstubbs', appVersion='0.1.0')
```
The output should look similar to the following:

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
inputMode: FIXED
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

## Next Steps
With our application registered, we are now ready to have Tapis execute our app by
submitting a job to the Jobs service.

[Next-> Executing the Classifier App](../jobs/hello.md)