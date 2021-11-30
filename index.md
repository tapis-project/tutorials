# Tapis Tutorials

Tapis is an NSF-funded API platform for computational research. This
website provides self-paced tutorials covering the primary Tapis concepts
and functionality. 

## About These Tutorials
These tutorials utilize the Python programming language to invoke calls to Tapis. All 
examples use the Tapis Python SDK (`tapipy`).  We assume familiarity with Python and basic Unix shell 
commands throughout these tutorials. We also assume the reader has a TACC account. See the 
[introduction](https://tapis-project.github.io/tutorials/intro/intro/) for more details.

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
it is probably best to start with the Introduction and work through the tutorial series in
the order that they appear in the left nav. Thus, move to the "Registering Systems and 
Managing Data" after the Introduction, then to "Creating Applications and Running Jobs",
etc. 

## Setting Up The Environment
A Unix operating system (i.e., Linux or Mac OSX) as well as a recent version of Python 3 
and the `tapipy` library are required to work through these tutorials (it is likely the
tutorials will work on WSL but this has not been extensively tested). Additionally, a 
working installation of a recent version of Docker (e.g., 20.10.11) is required to build
the applications.

We have provided a Docker image which can be used for all tutorials that includes all 
necessary software pre-installed.

To use it, first create a directory to hold your work:

```
$ mkdir tapis-tutorials
```

then start the container from the `tapis/jupyter` image, mounting in the directory

```
$ docker run -v $(pwd)/tapis-tutorials:/home/jovyan/data --rm -it -p 8888:8888 tapis/jupyter
```

The commmand above should have started a single container from the `tapis/jupyter` image, 
which prints out a url to access the jupyter notebook from the browser.
You can copy and paste this URL into your browser and access the jupyter notebook.