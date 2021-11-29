# Registering an HPC System
HPC systems usually rely on a batch scheduler such as Slurm to schedule jobs on a cluster
of machines. You can register an HPC cluster as a Tapis system to enable to Tapis to 
submit and monitor jobs on the cluster for you.

In this example, we will register the Stampede2 supercomputer at TACC. Registering 
Stampede2 with Tapis requires that your TACC account have a valid allocation on 
Stampede2. If you do not have an allocation on Stampede2, you can still use the concepts
illustrated in this tutorial to register another HPC cluster that you do have access to.

