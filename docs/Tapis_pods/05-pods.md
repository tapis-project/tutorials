# Introduction to Tapis Pods service
The Tapis Pods service provides easy-to-deploy network-accessible long-running Pods on demand. In this case, the physical manifestation of the service comes in the form of Kubernetes Pods in a private cluster networked through a dynamic proxy based off of this API.
The Pods service serves a niche for applications that don't require an all out VM, but still need reliable networking and round-the-clock availability.
Initially the service was created for databases, in particular Neo4j databases serving through a custom "Bolt" protocol. The project has been expanded since then and now allows for broad HTTP and TCP networking, even making room for custom protocols required for the likes of Postgres.

## Life cycle of Pods
When a job request is received as the payload of an POST call, the following steps are taken:

The goal of this service is to create a pod for a user based on the information given to us through the API. The pod creation is done using the Python `Kubernetes` client. With the tools in `kubernetes_utils.py` we're able to create, delete, update, and do whatever we want to Kubernetes pods, services, configmaps, certs, and more. 

The top-level overview of pod creation works is as follows. A user create a pod, by default said pod's `status_requested` is set to `ON`. In the POST to `/pods`, the service will create a database entry for the pod, and send a message with RabbitMQ requesting a new pod. That message will be read by `spawner.py`, in the `spawner` pod. The spawner will take the message and create the pod. After that, `health.py` in the `health` pod will take care of everything else. Health will poll every X seconds. It'll update pod database information based on what's happening to the pod ("Completed", "Running", new logs, etc). Health will also take care of updating the `pods-nginx` configmap with information found during the "healthcheck".


## Pod Workflow - With more precision.
**status_requested**: The user can set their pod to `ON`, `OFF`, or `RESTART`. This is used as an overall, "what do we want to do with the pod" field. Instead of using only the pod `status` field, we can use this to control workflow.
- **ON** - Create pod and get to `RUNNING` status. Default during `create_pod`. Can also be set by `start_pod`.
- **OFF** - Attempts to delete and get to `STOPPED` status. Can be set by `stop_pod`. This will disrupt and pod creation currently happening.
- **RESTART** - Functions as `OFF`. Set `status_requested` to `ON` once pod hits `STOPPED` status.

**status**: This is the internal state of the pod itself, what is actually happening to it, either in regards to only the service, or reflecting back the pod's status from Kubernetes itself.

- **Internal Statuses**
  - **REQUESTED** - Put into status when ON is noticed, either during `create_pod` or healthcheck.
  - **SPAWNER_SETUP** - Set when request msg is read and spawner attempts to create container
  - **CREATING_CONTAINER** - Set after create_pod and create_service is ran
  - **SHUTTING_DOWN** - Set once health starts trying to delete

- **Kubernetes Controlled Statuses**
  - **RUNNING** - Based off of Kubernetes
  - **ERROR** - Based off of Kubernetes
  - **COMPLETE** - Based off of Kubernetes
  - **STOPPED** - If pod + service not in Kubernetes, then status is `STOPPED`

**status_container**: Not that useful, but as we're creating Kubernetes pods, each pod is X containers (usually only 1 in our case). We reflect that for the users to have more data to debug. If a pod has container info, we display it (assumes only 1 container thus far).

## A Minimal Pod 
A minimal Pod declaration could looks like this:
```
{
    "pod_id": "myneo4jpod",
    "pod_template": "neo4j",
    "description": "A brief description of my Pod so I and others can remeber it's purpose."

}
```
where:
* **pod_id** - Required - Name of this pod.
* **pod_template** - Required - Which pod template to use, or which custom image to run (must be on allowlist).
* **description** - Description of this pod.


A few additional arguments that often get used are: 
* **command** - Command to run in pod, overriding default image command.
* **routing_port** - For custom pods, specify what port to expose in the Pod.
* **persistent_volume** - True/False on whether to mount a persistent volume to your Pod.
* **environment_variables**	- Environment variables to inject into k8 pod; Only for custom pods.
* **time_to_stop_default** - Time (sec) for pod to run from instance start before the service stops it.
* **time_to_stop_instance** - Specify time_to_stop for one particular instance.

The complete set of Pod submission parameters are listed here [Pod Submission Parameters](https://tapis-project.github.io/live-docs/?service=Pods#tag/Pods/operation/create_pod). All Pod endpoints are specified with inputs and outputs at the live-docs link above.

## Tutorial Pods
Users have restricted access to images and templates that they can run. Depending on the tenant, users might have some default images that they have access to. However, most users will have no images or templates that they are allowed to run. Users should reach out to a Tapis admin in order to add images or templates to their profiles.

During tutorials users should have access to a fastapi image and template:

Image definition:
```
{
  "image": "tiangolo/uvicorn-gunicorn-fastapi",
  "tenants": [
    "**"
  ],
  "description": "Official fastapi author. Runs a FastAPI app with Uvicorn and Gunicorn",
  "creation_ts": "2025-07-20T16:16:37.325Z",
  "added_by": "cgarcia"
}
```

Template definition:
```{
  "template_id": "fastapi",
  "description": "Collection of fastapi templates with different configurations.",
  "metatags": [
    "TACC",
    "API",
    "FastAPI"
  ],
  "archive_message": "",
  "creation_ts": "2025-07-21T17:35:06.723Z",
  "update_ts": "2025-07-21T17:35:06.723Z"
}
```

Creating a pod with Tapipy (python sdk) is done as so:

```
{
  "pod_id": "testid",
  "template": "fastapi:fastapinetworked"
}
```