# Introduction

The Tapis framework is an application programming interface (API) hosted in the cloud.
Using Tapis, computational researchers can manage data and execute software on a
variety of different systems, including virtual machines (VMs) and high-performance
computing (HPC) clusters. This website is a collection of self-paces tutorials for learning
how to incorporate Tapis into computational research.

Programming a computational experiment with Tapis affords the following benefits:
* _Automation_ - Researchers can use Tapis to automatically run workloads on 
different machines and even across different institutions.
* _Portability_ - Tapis makes it easier to run the same application on different machines.
* _Repeatability and Reproducibility_ - Tapis records the inputs and parameters that were used to execute
software allowing researchers and their collaborators to repeat prior job runs and reproduce results.
* _Collaboration_ - Researchers can keep their data, applications and results private or they can share 
them with their collaborators.

## Prerequisites
These tutorials assume access to and familiarity with the following topics:
* Basic Unix shell commands
* Python programming language and writing Python code in a REPL or Jupyter notebook.
* Docker containers

Additionally, the tutorials assume the reader has access to the following: 
* A TACC account (sign up for a TACC account [here](https://portal.tacc.utexas.edu/account-request))
* A working computer with Unix (Linux, Mac OSX) 
* A recent version of Docker installed (see instructions for [installing Docker](https://docs.docker.com/get-docker/) )

## Setting Up the Environment
A Unix operating system (i.e., Linux or Mac OSX) as well as a recent version of Python 3 and 
the `tapipy` library are required to work through these tutorials (it is likely the
tutorials will work on WSL but this has not been extensively tested). Additional libraries
such as `jupyter`, `numpy`, etc., are recommended. The `requirements.txt` file in the root
of this repository can be used to create a virtual environment with all requried and optional
packages.

Additionally, a working installation of a recent version of Docker (e.g., 20.10.11) is required to build
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

## Additional Resources
The following additional resources are also available to you:

* Tapis reference documentation: https://tapis.readthedocs.org
* Support via The TACC Cloud Slack (tacc-cloud.slack.com); Join here: http://bit.ly/join-tapis
* Tapis API specifications: https://tapis-project.github.io/live-docs/