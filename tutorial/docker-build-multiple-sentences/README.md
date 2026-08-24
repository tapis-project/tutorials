# docker_build
This folder can be used to build docker images in order to run `analyze_sentiment.py`.

***analyze_sentiment.py***
- Python script performing sentiment analysis on data provided by user.

# Docker Image Handling
> This is assuming that docker is already installed on the system.

## Running the image:
To run the image, run this command:
```bash
$ docker run tapis/sentiment-analysis:1.0.1 <arguments>
```
There are multiple arguments built into this application. Here are your options:
|Arguments|Explanation|Options|Example|
|---|---|---|---|
|sentence|The sentence to analyze. (Technically optional, but that's no fun)|Anything|--sentence='I love potatoes'|
|model|Model to use. (Optional)|[Link](https://huggingface.co/models?pipeline_tag=text-classification&sort=downloads)|--model='j-hartmann/emotion-english-distilroberta-base'|
|return all scores|Choose to either return all or only one score. Anything other than f or false is considered as true. Capitalization does not matter. (Optional since the default is "True")|f, false, true|--return_all_scores='false'| 

> Example of running the image with default model
> ```bash
> $ docker run --user $(id -u):$(id -g) --mount type=bind,source=/tmp,target=/tmp tapis/sentiment-analysis:1.0.1 --sentence='I love potatoes'
> ```

> Example of running the image with all arguments:
> ```bash
> $ docker run --user $(id -u):$(id -g) --mount type=bind,source=/tmp,target=/tmp tapis/sentiment-analysis:1.0.1 --sentence='I love potatoes' --model='j-hartmann/emotion-english-distilroberta-base' --return_all_scores='f'
> ```
> Output:
> ```
> Downloading: 100%|##########| 0.98k/0.98k [00:00<00:00, 1.21MB/s]
> Downloading: 100%|##########| 313M/313M [00:04<00:00, 69.4MB/s] 
> Downloading: 100%|##########| 294/294 [00:00<00:00, 574kB/s]
> Downloading: 100%|##########| 780k/780k [00:00<00:00, 22.2MB/s]
> Downloading: 100%|##########| 446k/446k [00:00<00:00, 4.60MB/s]
> Downloading: 100%|##########| 1.29M/1.29M [00:00<00:00, 8.47MB/s]
> Downloading: 100%|##########| 239/239 [00:00<00:00, 419kB/s]The sentence,I love potatoes
> joy,97.50%
> ```

Results will be saved in `/tmp/results.csv`.

## Pulling the image:
To pull the existing image, run this command:
```bash
$ docker pull tapis/sentiment-analysis:1.0.1
```
The image should now be available on the local host:
```bash
$ docker images
```
> The output should look similar to this:
> ```
> REPOSITORY                    TAG    IMAGE ID       CREATED         SIZE
> tapis/sentiment-analysis      1.0.1  d8276d24fa21   2 hours ago     897MB
> ```

## Building the image:
To build the image, run this command:
```bash
$ docker build -t tapis/sentiment-analysis:1.0.1 .
```
