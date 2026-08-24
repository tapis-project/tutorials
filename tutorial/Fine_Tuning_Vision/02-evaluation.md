# Section 10: Evaluating Fine-tuned Model by Running Code Detection On Jupyter [Hands-On]

We use our Jupyter Notebook Environment to run the evaluation code on the test dataset and see the accuracy of our fine-tuned model.


## Starting up your Jupyter Notebook Environment

For this tutorial, we will use <a href="https://public.jupyter.tacc.cloud" target="_blank">TACC's Public JupyterHub</a> 
You may login with your TACC accounts.

### Navigating to the $WORK File System

On successful login, ensure that you have access to a folder, `work`, within the Jupyter file system. 

### Restarting your Jupyter Server

Click on **Files** -> **Hub control panel** -> **Stop my server** -> **Start server**

## Running the evaluation code

Go to the Jupyter notebook Code-Detection on your Jupyter path. 
`ai-tutorial-2026 -> notebooks -> Code-Detection.ipynb`

Copy the generated code from FlexServ UI in a new cell below the cell titled `Put your generated code here`. 

Make sure the variable `DATASET_ROOT` is set to path `/home/jovyan/ai-tutorial-2026/datasets/AnimalEcology.v4i.yolov11` in your generated code. 

Make sure the variable `BASEURL` is set to the Base URL of your FlexServ and `FLEXSERV_TOKEN` is set to your FlexServ token.

![Variables](/tutorials/images/sec8/image17.png)

Running the code in Jupyter, and you should be able to see the evaluation result similar to below

![Variables](/tutorials/images/sec8/image18.png)

In the code, you can easily switch `MODEL_TO_USE` between `BASE_YOLO_MODEL` and `FINE_TUNED_YOLO_MODEL` to switch between the base model and the fine-tuned model. 



<!-- ## Section 9: Evaluating the Fine-tuned Model 

To try this part of the tutorial, we will use the fine-tuned model `best.pt` created by the ultralytics-fine-tune job.

### Step 9.1: Locate your Fine-tuned model

Once your job is complete, your fine-tuned model will be accessible through Jupyter in this location
`$WORK -> vista -> jobUUID -> train -> weights -> best.pt`

Please locate your file location. 

### Step 9.2: Point your Jupyter notebook code at your Fine-tuned model location

You should already have the generated code that we tested accuracy on the baseline model.

Now, just change the path of your model to the fine-tuned model path and re-run the code to test the accuracy.

### Step 9.3: Re-run the notebook

When the code runs on the test data, you should see improved accuracy

```
Evaluation Metrics:
Total images processed: 100
Total animal images on (based label files): 71
True Positives: 50
True Negatives: 25
False Positives: 4
False Negatives: 21
Overall detection accuracy: 0.75
```

As an exercise, you may train your model with more epochs and see if this accuracy can be further improved. -->
