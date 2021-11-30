# Tapis Tutorials

Tapis is an NSF-funded API platform for computational research. This
website provides self-paced tutorials covering the primary Tapis concepts
and functionality. 

## About These Tutorials
These tutorials utilize the Python programming language to invoke calls to Tapis. All 
examples use the Tapis Python SDK (`tapipy`).  We assume familiarity with Python and basic Unix shell 
commands throughout these tutorials. We also assume the reader has a TACC account. See the 
[Introduction](intro/intro.md) for more details.

## How To Use These Tutorials
Each tutorial is a short and (relatively) self-contained unit covering a single topic.
If you know what you want to do, in theory, you should be able to jump straight to the 
tutorial covering the partical topic. For example, if you are interested in working
with S3 in Tapis, you might want to jump straight to the tutorial on 
[Registering an S3 Bucket](systems/s3.md).

While the tutorials are constructed to be modular units, some of them also naturally
build on each other to form a series. We have collected some of these into tutorial series
which can be found in the left nav. The "Registering Systems and Managing Data" series
and the "Creating Applications and Running Jobs" are two examples.

If you are entirely new to Tapis and just want to get a general sense for its capabilities,
it is probably best to start with the [Introduction](intro/intro.md) and work through the 
tutorial series in
the order that they appear in the left nav. Thus, move to the "Registering Systems and 
Managing Data" series after the Introduction, then to the "Creating Applications and 
Running Jobs" series, etc. 

## Setting Up The Environment
Details about setting up the environment are provided in the [Introduction](intro/intro.md).

If you are rearing to get started, you can use the Docker image we have provided for all 
tutorials; it includes all necessary software pre-installed.

To use it, first create a directory to hold your work:

```
$ mkdir tapis-tutorials
```

then start the container from the `tapis/jupyter` image, mounting in the directory

```
$ docker run -v $(pwd)/tapis-tutorials:/home/jovyan/data --rm -it -p 8888:8888 tapis/jupyter
```

The command above should have started a single container from the `tapis/jupyter` image, 
which prints out a url to access the jupyter notebook from the browser.
You can copy and paste this URL into your browser and access the jupyter notebook.