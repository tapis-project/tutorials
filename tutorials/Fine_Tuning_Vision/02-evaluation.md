## Evaluating the Fine-tuned Model 

To try this part of the tutorial, we will use the fine-tuned model `best.pt` created by the ultralytics-fine-tune job.

Your fine-tuned model will be accessible through Jupyter in this location
`$WORK -> vista -> jobUUID -> train -> weights -> best.pt`

You should already have the generated code that we tested accuracy on the baseline model.

Now, just change the path of your model to the fine-tuned model path and re-run the code to test the accuracy.

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

As an exercise, you may train your model with more epochs and see if this accuracy can be further improved.
