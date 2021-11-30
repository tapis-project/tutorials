# Introduction

The Tapis framework is an application programming interface (API) hosted in the cloud.
Using Tapis, computational researchers can manage data and execute software on a
variety of different systems, including bare metal servers, virtual machines (VMs) and 
high-performance computing (HPC) clusters. This website contains a collection of self-paced 
tutorials for learning how to incorporate Tapis into computational research workflows.

Programming a computational experiment with Tapis affords the following benefits:
* _Workflow Automation_ - Researchers can use Tapis to automatically run workloads on 
different machines and even across different institutions.
* _Application Portability_ - Tapis makes it easier to run the same application on different machines.
* _Repeatability and Reproducibility_ - Tapis records the inputs and parameters that were used to execute
software, allowing researchers and their collaborators to repeat prior job runs and reproduce results.
* _Collaboration_ - Researchers can keep the data, applications and results they register with 
Tapis private, or they can share them with one or more collaborators. Tapis helps researchers
disseminate their work to the larger community.

## Prerequisites
These tutorials assume access to and familiarity with the following topics:
* Basic Unix shell commands
* The Python programming language and writing Python code in a REPL or Jupyter notebook
* The Docker container runtime

Additionally, the tutorials assume the reader has access to the following: 
* A TACC account (sign up for a TACC account [here](https://portal.tacc.utexas.edu/account-request))
* A working computer with Unix (i.e., Linux or Mac OSX). Windows Subsytem for Linux may also work 
but is not extensively tested
* A recent Python 3 installation (e.g., 3.5+)
* Installation of the `tapipy` Python package.
* A recent version of Docker (e.g., 20.10+) installed (see instructions for [installing Docker](https://docs.docker.com/get-docker/) )

## Setting Up the Environment
A Unix operating system (i.e., Linux or Mac OSX) as well as a recent version of Python 3 and 
the `tapipy` library are required to work through these tutorials (it is likely the
tutorials will work on WSL but this has not been extensively tested). Additional libraries
such as `jupyter`, `numpy`, etc., are recommended. The `requirements.txt` file in the root
of this repository can be used to create a virtual environment with all required and optional
packages.

Additionally, a working installation of a recent version of Docker (e.g., 20.10.11) is required to build
the applications.

We have provided a Docker image which can be used for all tutorials that includes all 
necessary software pre-installed. To use it, first create a directory to hold your work:

```
$ mkdir tapis-tutorials
```

then start the container from the `tapis/jupyter` image, mounting in the directory:

```
$ docker run -v $(pwd)/tapis-tutorials:/home/jovyan/data --rm -it -p 8888:8888 tapis/jupyter
```

If all goes well, you should see a message indicating that the notebook server started up.
The output should be similar to:

```python
[I 18:10:38.466 NotebookApp] Jupyter Notebook 6.4.4 is running at:
[I 18:10:38.466 NotebookApp] http://2f8af6573099:8888/?token=30970be8730c505efcf4d760a92d0774a28da30c84ba6c51
[I 18:10:38.466 NotebookApp]  or http://127.0.0.1:8888/?token=30970be8730c505efcf4d760a92d0774a28da30c84ba6c51
[I 18:10:38.466 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
Copy and paste the full URL including the token into your browser.

## Starting up your Jupyter Notebook Environment

Your jupyter notebook server should be already running at `http://127.0.0.1:8888/?token=` (The one you got in the 
previous section after running the docker container). You can reach it by going to 
that location in a browser window.

Once you open a browser with your Jupyter environment, you should see something similar 
to this: 

<img src="../images/jupyter1.png" class="img-responsive" alt="Jupyter interface"> 

## Creating a New Notebook

To create a new notebook for writing code, start by clicking 'New' in the upper right 
corner. From here, you will be able to choose what type of notebook you want. For this 
tutorial, we will be using Python 3. 

<img src="../images/jupyter2.png" alt="Jupyter Notebook">

Once you open a notebook, you can write and run python code. To execute a line of code, 
press `shift + Enter`. 

## Next Steps
With the environmnet setup, we're now ready for the Hello, Tapis tutorial.
[Next-> Hello, Tapis](../hello/hello.md)

## Additional Resources
The following additional resources are also available to you:

* Tapis reference documentation: https://tapis.readthedocs.org
* Support via The TACC Cloud Slack (tacc-cloud.slack.com); Join here: http://bit.ly/join-tapis
* Tapis API specifications: https://tapis-project.github.io/live-docs/