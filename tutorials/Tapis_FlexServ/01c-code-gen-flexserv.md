# FlexServ API Prompt: YOLO Evaluation Script Generator

### Task Summary:
To test the capabilities of the FlexServ inference server, we can provide a complex prompt to the Responses API. This prompt asks the AI to generate a complete Python evaluation script that performs Animal detection on the images from the LILA BC Small Animal dataset. This is a large camera-trap image dataset used for wildlife monitoring and ecological research. It contains millions of images captured by automated cameras, including small mammals and many blank triggers, along with annotations describing the detected species. For training object detection models such as YOLO, the dataset can be downloaded in YOLO format, where each image has a corresponding .txt label file containing normalized bounding-box coordinates in the form <class_id> <x_center> <y_center> <width> <height>.

---

### On FlexServ UI

1. Copy and paste the following text into the FlexServ UI in the `Responses API`, `Input(Markdown)` section 
![Paste Prompt](/tutorials/images/Paste_Prompt.png)

<div style="max-height:400px; overflow:auto; border:1px solid #ddd; padding:10px;">
<pre>

> "Write Python code that reads all images from a dataset root directory stored in the variable DATASET_ROOT.
>
> **TASK DESCRIPTION:**
> - This is an IMAGE-LEVEL BINARY CLASSIFICATION task implemented using an object detection model.
> - The goal is to determine whether an image contains an animal or not.
>
> **DATASET STRUCTURE:**
> - DATASET_ROOT contains three subdirectories: `train`, `test`, and `val`.
> - Each directory contains two subdirectories:
>   * images/ → contains image files (.jpg, .jpeg, .png)
>   * labels/ → contains YOLO format .txt files
> - GROUND-TRUTH LOGIC: An image is considered an `animal` if a corresponding .txt file exists and is not empty in the `labels/` folder.
>
> **MODEL REQUIREMENTS:**
> - Use ONLY a pretrained Ultralytics YOLO detection model (e.g., yolov8n.pt).
> - Load the model using the Ultralytics YOLO API.
> - Assume YOLO detects animals using class ID `animal` at index 0.
>
> **DETECTION LOGIC (IMPORTANT):**
> - Run object detection on each image.
> - If the model produces AT LEAST ONE detection of an animal class with confidence >= 0.5:
>     → The image-level prediction is `animal`.
>
> **EVALUATION METRICS:**
> - Iterate through the images in the `test` split.
> - Compare the image-level prediction with the ground truth (existence of label file).
> - Count: True Positives, True Negatives, False Positives, and False Negatives.
>
> **ACCURACY DEFINITION:**
> - Overall accuracy = (True Positives + True Negatives) / Total Images
>
> **OUTPUT REQUIREMENTS:**
> - Print for each image: filename, ground-truth status, and prediction.
> - At the end, print a summary report including total images, counts for each metric, and overall detection accuracy.
>
> **CODING REQUIREMENTS:**
> - Store the main path in DATASET_ROOT.
> - Use `pathlib` or `os` for robust file path matching.
> - Read only .jpg, .jpeg, and .png files.
> - Include clear comments explaining each step.
>
> After the code, briefly explain how the program works in plain English."
</pre>
</div>

2. Change the temperature to 0.0 for a deterministic solution.
3. Select the model to Run
    -   Qwen/Qwen2.5-Coder32B-Instruct-61.0 GB - Text Generation
4. Make sure the Streams is checked. 
5. Uncheck Multi-turn conversation
6. Click Run. You should see the generated code in the blue box in Responses API. Wait for it to complete.

![Code](/tutorials/images/Code.png)

Now, let's test it's performance on the test dataset using the Jupyter Notebook.


### On Jupyter :

Go to the notebook Code-Detection on your Jupyter
ai-tutorial-2026 -> notebooks -> Code-Detection.ipynb

Copy the generated code from FlexServ UI in a new cell below the cell titled `Put your generated code here`. 

Update the variable `DATASET_ROOT` to path `/home/jovyan/work/vista/ai-tutorial-2026/datasets/AnimalEcology.v4i.yolov11` in your generated code

Also update the model path to `/home/jovyan/work/vista/ai-tutorial-2026/models/yolov9t_ep200_bs32_lr0.005_baa22147.pt`

Now run the code. On successful run, you should see output similar to below 

<div style="max-height:400px; overflow:auto; border:1px solid #ddd; padding:10px;">
<pre>

image 1/1 /home/jovyan/work/vista/ai-tutorial-2026/datasets/AnimalEcology.v4i.yolov11/test/images/KPC2__2019-09-19__15-47-42-1-_JPG.rf.608031a2809f0f6714f175d3e5eb7f06.jpg: 640x640 1 animal, 96.6ms
Filename: KPC2__2019-09-19__15-47-42-1-_JPG.rf.608031a2809f0f6714f175d3e5eb7f06.jpg, Ground Truth: no_animal, Prediction: animal

Speed: 2.5ms preprocess, 96.6ms inference, 1.0ms postprocess per image at shape (1, 3, 640, 640)
image 1/1 /home/jovyan/work/vista/ai-tutorial-2026/datasets/AnimalEcology.v4i.yolov11/test/images/NOR3__2019-07-19__11-40-00-1-_JPG.rf.b85ee30f99a803b09f8c5a7da7f9a508.jpg: 640x640 (no detections), 104.2ms
Speed: 1.9ms preprocess, 104.2ms inference, 0.7ms postprocess per image at shape (1, 3, 640, 640)
Filename: NOR3__2019-07-19__11-40-00-1-_JPG.rf.b85ee30f99a803b09f8c5a7da7f9a508.jpg, Ground Truth: animal, Prediction: no_animal
....
...
Evaluation Metrics:
Total images processed: 100
Total animal images (based on label files): 71
True Positives: 47
True Negatives: 6
False Positives: 23
False Negatives: 24
Overall detection accuracy: 0.53
</pre>
</div>

