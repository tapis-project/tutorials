# Ultralytics Fine-Tuning App

This application allows users to fine-tune Ultralytics YOLO models using Singularity containers in a batch processing environment. It is designed to run on High-Performance Computing (HPC) systems via Tapis, leveraging GPU acceleration for training tasks.

> **Note:** This app is already registered for the tutorial and is available to run via the Tapis UI.

---

## App Definition

The following JSON represents the application definition used to register the fine-tuning service in Tapis:

```json
{
    "id": "ultralytics-fine-tune",
    "version": "0.1",
    "description": "An app to fine-tune ultralytics Yolo using Singularity in batch mode.",
    "jobType": "BATCH",
    "runtime": "SINGULARITY",
    "containerImage": "/work/projects/aci/cic/apps/ultralytics-fine-tune/Ultralytics_FT_Tapis_app.sif",
    "jobAttributes": {
        "execSystemExecDir": "${JobWorkingDir}/jobs/${JobUUID}",
        "execSystemInputDir": "${JobWorkingDir}/jobs/${JobUUID}/data",
        "execSystemOutputDir": "${JobWorkingDir}/jobs/${JobUUID}/output",
        "parameterSet": {
            "containerArgs": [
                {
                    "name": "nvidia",
                    "inputMode": "FIXED",
                    "arg": "--nv",
                    "notes": {}
                }
            ],
            "envVariables": [
                {
                    "key": "EPOCHS",
                    "value": "3",
                    "description": "Number of epochs for the fine-tune job",
                    "inputMode": "REQUIRED",
                    "notes": {}
                }
            ]
        },
        "memoryMB": 1,
        "nodeCount": 1,
        "coresPerNode": 1,
        "maxMinutes": 10
    }
}
```
# Understanding Ultralytics App Parameters

The `ultralytics-fine-tune` application uses a specific set of parameters to manage how the Singularity container interacts with the HPC hardware and how the training process is executed.

---

## 1. Container Arguments
Container arguments define how the Tapis runtime (Singularity) is initialized on the execution system.

| Parameter | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| **nvidia** | `FIXED` | `--nv` | This is the most critical argument. It tells Singularity to bind the host's NVIDIA drivers inside the container, enabling GPU acceleration for YOLO training. |



---

## 2. Environment Variables
Environment variables are passed into the training script inside the container to control the YOLO model's behavior.

| Variable | Mode | Default | Description |
| :--- | :--- | :--- | :--- |
| **EPOCHS** | `REQUIRED` | `3` | Defines the number of full passes through the training dataset. For this tutorial, it is set low (3) to ensure quick completion, but can be increased for real-world accuracy. |

---

## 3. Resource Attributes
These parameters define the hardware footprint requested from the Slurm scheduler on the execution system.

* **Node Count (`1`):** The number of physical machines requested. Fine-tuning for this tutorial is optimized for a single node.
* **Cores Per Node (`1`):** The number of CPU cores allocated. Since the primary work is done by the GPU (via the `--nv` flag), CPU requirements are kept minimal.
* **Memory (`1 MB`):** The RAM allocation. *Note: In many Tapis configurations, 1 implies a minimum default or is managed by the specific queue policy.*
* **Max Minutes (`10`):** The "Wallclock" time. If the job exceeds 10 minutes, the scheduler will terminate it to prevent hanging processes from wasting allocation credits.





---

> **Note:** These parameters are pre-configured for the tutorial. When using the Tapis UI, you will primarily interact with the **EPOCHS** variable.