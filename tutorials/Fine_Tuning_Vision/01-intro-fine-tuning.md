# Section 4: Ultralytics Fine-Tuning App


[Lecture Slides](https://docs.google.com/presentation/d/1l13lRedG7Bp0_nguU6zxvOOEanGdzqsIFLlCTZ8FIvY/edit?slide=id.g3cd6a51b6a2_0_42#slide=id.g3cd6a51b6a2_0_42){:target="_blank"}


<div style="
  position:relative;
  width:100%;
  height:450px;
  overflow:hidden;
  border:1px solid #d9e0ea;
  border-radius:12px;
">
  <iframe
    src="{{ '/assets/FlexServ_AI_Closed_Loop.html' | relative_url }}?step-to-show=2"
    title="FlexServ AI closed loop — Fine-tuning"
    style="
      position:absolute;
      inset:0;
      width:200%;
      height:900px;
      border:0;
      transform:scale(0.5);
      transform-origin:top left;
    ">
  </iframe>
</div>

<p>
  <a href="{{ '/assets/FlexServ_AI_Closed_Loop.html' | relative_url }}?step-to-show=2"
     target="_blank"
     rel="noopener">
    Open the interactive diagram in a new tab
  </a>
</p>

In the previous section, the YOLO 26 base model `yolo26n` has been downloaded to FlexServ private model pool, and this fine-tuning task will use that as a base model and fine-tune it using a set of camera-trap images. The fine-tuned model will be save into FlexServ private model pool, and later we will generate model performance evaluation code using FlexServ, and run that code in our Jupyter Notebook Environment. The evaluation code will send camera-trap images to our yolo inference API in FlexServ to get the model inference result and compare that with the ground truth labels in our Jupyter Notebook Environment to get the model evaluation result. 

This application allows users to fine-tune Ultralytics YOLO 26 models using Singularity containers in a batch processing environment. 

It is designed to run on High-Performance Computing (HPC) systems via Tapis, leveraging GPU acceleration for training tasks.

> **Note:** This app is already registered for the tutorial and is available to run via the Tapis UI.

---

## Locating the App and Configure Job Submission

Login to [public.tapis.io](https://public.tapis.io){:target="_blank"} using your TACC username and password.

Go to the **App** tab and find the app with name `yolo-finetuning-arm64`. 

![App definition](/tutorials/images/sec8/image1.png)

Click on the **Submit Job** button to and then click on the **USE GUIDED JOB LAUNCHER** button.

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image2.png)

Now we are in the job configuration interface. 

<!-- Click **Continue** on the job summary page. -->

<!-- ![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image3.png) -->

In the **Execution** page, select the following: 

  1. Execution System - `vista-test-nairr`
  2. Job Type - `Batch`
  3. Batch Logical Queue - `gh-shared`

<!-- Click **Continue**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image4.png) -->



![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image5.png)

Click **Environment**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image8.png)


There are 4 environment variables important for the fine-tuning job. 

 1. EPOCHS - number of learning rounds. 10 or 20 is a good number.
 2. YOLO_26_MODEL - the yolo model name. Here we use `yolo26n` for the best trade-off between quality and speed. Note that you have to make sure you used `yolo26n` model previously during the FlexServ section so that the `yolo/yolo26n` model shows up in your private model pool of your FlexServ. If you happen to have used a different yolo26 model during our FlexServ section, say `yolo26l`, you should put `yolo26l` here for `YOLO_26_MODEL` instead.
 3. TWO_STAGE_FINE_TUNE - If true, we use two-stage fine-tuning process where the first stage freezes the backbone and trains only the neck and head, allowing the detection layers to adapt to the new classes without disrupting pretrained features. The second stage unfreezes all layers and trains the full model with a lower learning rate to refine the backbone for the target domain.
 4. The freeze parameter accepts an integer. An integer freeze=10 freezes the first 10 layers (0 through 9, which corresponds to the backbone in YOLO26). This speeds up training and reduces overfitting when the dataset is small relative to the model capacity.

<!-- Just keep all these settings as is, and click **Continue**. -->

Go back to FlexServ UI, click on "Models" on the left navigation panel, and you can scroll up and down to see if you have a yolo model named `yolo/yolo26n` there in your private model pool. 

![FlexServ API Tests - Yolo Inference API - What happens to your model pool](/tutorials/images/sec3/image32.png)

This is because we have run yolo inference test during our FlexServ section. 

Since the yolo model you see is `yolo26n`, that means you should fill `yolo26n` in the `YOLO_26_MODEL` field. 

Now click on **Scheduler**

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image9.png)

In Scheduler tab, you need to fill the following: 

 1. For **-A allocation**, put `TRA24006`
 2. For **--reservation**, put `Tapis+Tutorial+Gateways`





After this, you can click on **Review & submit**

<!-- ![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image10.png) -->

## Submit the job

Click **Submit Job**, and this should submit your job. 

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image11.png)

Click **Open Job** and you should see the submitted job. 

It can take roughly 5-10 minutes to finish the job, but depending on the job waiting time, it can be even longer.

![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image10.png)

But once finished, you can open the tapisjob.out file and view it. At the end of the output, you should see message indicating that the fine-tuned models are now saved to FlexServ's private model pool (`$SCRATCH/flexserv/models`). 


![USE GUIDED JOB LAUNCHER](/tutorials/images/sec8/image12.png)

Back to the FlexServ UI, in the model pool view, you should be able to see the `yolo/yolo26n-fine-tuned` model in your private model pool. 

![FlexServ API Tests - Yolo Inference API - What happens to your model pool](/tutorials/images/sec3/image32.png)

## Up Next

Now, we wonder how well the fine-tuned model works as compared to the original one.
In our model evaluation section, we will use a recently-released Qwen LLM in FlexServ to generate a python code that will call the Yolo inference API in FlexServ to perform the object detection inference using both the `yolo26n` based model and the `yolo26n-fine-tuned` model. We can see the difference in terms of the accuracy of these two models. 


