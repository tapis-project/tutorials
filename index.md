# Tapis Tutorials

Tapis is an NSF-funded API platform for computational research. This
website provides self-paced tutorials covering the primary Tapis concepts
and functionality. 

## About These Tutorials
These tutorials utilize the Python programming language to invoke calls to Tapis. All 
examples use the Tapis Python SDK (`tapipy`).  We assume familiarity with Python and basic Unix shell 
commands throughout this tutorial. We also assume the reader has a TACC account. See the 
[introduction](https://tapis-project.github.io/tutorials/intro/intro/) for more details.

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