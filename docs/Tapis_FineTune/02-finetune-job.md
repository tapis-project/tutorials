# Submitting an Ultralytics Fine-Tuning Job

Once the application is registered, you can submit a specific job to the execution system (e.g., Vista). This process involves defining the job's identity, the target resources, and the specific training parameters.

---

## Job Submission Payload

The following JSON represents a standard request to start a fine-tuning job:

```json
{
    "name": "ultralytics-fine-job",
    "appId": "ultralytics-fine-tune",
    "appVersion": "0.1",
    "execSystemId": "vista-test-nairr",
    "parameterSet": {
      "schedulerOptions": [ 
          { "name": "Allocation", "arg": "-A <insert here>" }, 
          { "name": "Reservation", "arg": "--reservation GHTapis+Nairr" }
      ],
      "envVariables": [
          {
              "key": "EPOCHS",
              "value": "100"
          }
      ]
    }
}
```
# Job Parameters

The following parameters are used to define the specific execution requirements for your Ultralytics fine-tuning job.

### 1. Identification
* **`name`**: A user-defined label for the job. This helps you identify the run in your job history.
* **`appId` & `appVersion`**: These link the job to the specific `ultralytics-fine-tune` app definition created earlier.
* **`execSystemId`**: Specifies the HPC resource where the job will run (e.g., `vista-test-nairr`).

### 2. Scheduler Options
These are specific flags passed to the Slurm scheduler on the Vista system:

* **Allocation (`-A`)**: You must replace `<insert here>` with your specific project account or allocation name. This is required for billing and resource tracking.
* **Reservation (`--reservation`)**: If you are part of a specific workshop or have reserved nodes, you include the reservation name here.

### 3. Environment Variables
* **`EPOCHS`**: In this job submission, the value is set to `100`. This overrides the default value of `3` in the app definition, allowing for a more thorough training session.

---

# UI Submission Walkthrough

Follow these steps to submit the job using the Tapis UI:

### Step 1: Initiate Submission
Navigate to the **Apps** list and select the `ultralytics-fine-tune` app. Click the button to initiate a JSON-based submission.

![Step 1 - Selecting the Ultralytics App in UI](/docs/images/Step1-Ultralyticsapp.png)

### Step 2: Edit the JSON Payload
Paste the job JSON provided above into the editor. Make sure to replace the `<insert here>` placeholders with your actual **Allocation** details and click `Submit`.

![Step 2 - Pasting the Job JSON into the Editor and Submit](/docs/images/Step2-Submit-fine-tune-job.png)

### Step 3: Monitor Job Progress
After clicking **Submit**, navigate to the **Jobs** tab. You can monitor the status as it moves from `PENDING` to `RUNNING` and finally `FINISHED`.

![Step 3 - Monitoring Job Status in the Dashboard](/docs/images/fine-tune-job-running.png) 
Since we are running 100 Epochs to fine-tune, this will take around 15-20 mins to finish.

### Step 4: Job Output and Results location
 Once the job finishes, you should see output similar to the image below.
 ![Step 4 - After Job completes](/docs/images/fine-tune-job-completion.png) 
 
 You should see a train directory with weights. Inside weights, you can access the best.pt model. This file will be accessible to you Jupyter.

### Step 5: Finding best.pt file from Jupyter 

Inside your work directory, you should see a vista folder. In there you can find the directory named with your job uuid. In the above image the job uuid is highlighted. In the job directory you will find the outputs of the job archieved with the same train directory containing the best.pt file.
`$WORK -> vista -> jobUUID -> train -> weights -> best.pt`
