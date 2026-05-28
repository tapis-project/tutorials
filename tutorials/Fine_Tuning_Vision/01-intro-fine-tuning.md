<style>
img {
  box-shadow: 0 0 .7rem rgba(0, 0, 0, 0.5);
}
.scrollable {
  max-height: 500px;
  overflow: auto;
}
</style>

# Ultralytics Fine-Tuning App

This application allows users to fine-tune Ultralytics YOLO 26 models using Singularity containers in a batch processing environment. It is designed to run on High-Performance Computing (HPC) systems via Tapis, leveraging GPU acceleration for training tasks.

> **Note:** This app is already registered for the tutorial and is available to run via the Tapis UI.

---

## Locating the App and Configure Job Submission

Go to the **App** tab and find the app with name `yolo-finetuning-arm64`. 

![App definition](/tutorials/images/sec8/image1.png)

Click on the **Submit Job** button to and then click on the **USE GUIDED JOB LAUNCHER** button.

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image2.png)

Now we are in the job configuration interface. Click **Continue** on the job summary page.

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image3.png)

In the **Execution Options** page, select the following: 

  1. Execution System - `vista-test-nairr`
  2. Job Type - `Batch`
  3. Batch Logical Queue - `gh`

Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image4.png)

Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image5.png)

Click **Continue**


![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image6.png)

Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image7.png)

There are 4 environment variables important for the fine-tuning job. 

 1. EPOCHS - number of learning rounds. 10 or 20 is a good number.
 2. YOLO_26_MODEL - the yolo model name. Here we use `yolo26n` for the best trade-off between quality and speed.
 3. TWO_STAGE_FINE_TUNE - If true, we use two-stage fine-tuning process where the first stage freezes the backbone and trains only the neck and head, allowing the detection layers to adapt to the new classes without disrupting pretrained features. The second stage unfreezes all layers and trains the full model with a lower learning rate to refine the backbone for the target domain.
 4. The freeze parameter accepts an integer. An integer freeze=10 freezes the first 10 layers (0 through 9, which corresponds to the backbone in YOLO26). This speeds up training and reduces overfitting when the dataset is small relative to the model capacity.

Just keep all these settings as is, and click **Continue**.

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image8.png)

Expand **TACC Resource Allocation** and **Reservation Name**
 1. For **TACC Resource Allocation**, put a space and then `TRA24006` after `-A`
 2. For **Reservation Name**, put a space and then your *reservation code* after `--reservation`

Note that the reservation code for **Sunday** sessions is `Tapis+Tutorial-Sun` and the reservation code for **Monday** sessions is `Tapis+Tutorial-Mon`.

Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image9.png)

Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image10.png)


## Submit the job

Click **Submit Job**, and this should submit your job. 

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image11.png)

It can take roughly 5-10 minutes to finish the job, but depending on the job waiting time, it can be even longer.

But once finished, you can open the tapisjob.out file and view it. At the end of the output, you should see message indicating that the fine-tuned models are now saved to FlexServ's private model pool (`$SCRATCH/flexserv/models`). 

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image12.png)

## Up Next

In our prompt engineering section, we will use a coding LLM in FlexServ to generate a python code that will call the Yolo inference API in FlexServ to perform the object detection inference using both the `yolo26n` based model and the `yolo26n-fine-tuned` model. We can see the difference in terms of the accuracy of these two models. 
