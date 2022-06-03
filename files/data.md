# Managing Data on a System

Now that we have a system created and a credential registered, we can now start using Tapis
to do some **real** work. In this short tutorial, we will use the Files API to get a file
listing on a directory, upload a file to the directory, and download a file.

## Listing Files in a Directory
To list files on a path, use the `listFiles()` endpoint of the `files` service, like so:

```pythonx
t.files.listFiles(systemId='<system_id>', path="/some/path")
```
replacing `<system_id>` with the system id and `/some/path` with the path on the system
you want to list. Note that `/some/path` is relative to the `rootDir` of the system; that
is, Tapis will prepend the `rootDir` path defined for the system to the `path` you 
provide. In this example system we created, `/` is the the rootDir and `work2` is the working directory created in the system initialization script. 

For example, to list files on our Stampede2 system, we could use a call like this:
```python
t.files.listFiles(systemId='stampede2.jstubbs', path="/work2/01837/jstubbs/stampede2")
```
And produces the following output:
```
[ 
 group: 814212
 lastModified: 2019-05-07T17:21:01Z
 mimeType: None
 name: bar
 nativePermissions: rw-r--r--
 owner: 811324
 path: /work2/01837/jstubbs/stampede2/bar
 size: 0
 type: file
 url: tapis://stampede2.jstubbs-2/work2/01837/jstubbs/stampede2/bar,
 
 group: 814212
 lastModified: 2021-10-27T14:38:14Z
 mimeType: None
 name: baz
 nativePermissions: rw-r--r--
 owner: 811324
 path: /work2/01837/jstubbs/stampede2/baz
 size: 0
 type: file
 url: tapis://stampede2.jstubbs-2/work2/01837/jstubbs/stampede2/baz,
 
 group: 814212
 lastModified: 2019-05-07T14:10:22Z
 mimeType: None
 name: foo
 nativePermissions: rwxrwxrwx
 owner: 811324
 path: /work2/01837/jstubbs/stampede2/foo
 size: 0
 type: file
 url: tapis://stampede2.jstubbs-2/work2/01837/jstubbs/stampede2/foo,
 
 group: 814212
 lastModified: 2021-12-02T00:03:44Z
 mimeType: None
 name: jobs
 nativePermissions: rwx------
 owner: 811324
 path: /work2/01837/jstubbs/stampede2/jobs
 size: 4096
 type: dir
 url: tapis://stampede2.jstubbs-2/work2/01837/jstubbs/stampede2/jobs]
 ```

## Uploading Files
We can upload a file with the following command:
```python
t.upload(system_id='<system_id>', 
         source_file_path='/some/local/file.txt', 
         dest_file_path="/some/remote/file.txt")

```
For example:
```python
t.upload(system_id='stampede2.jstubbs', 
         source_file_path='hello-tapis.ipynb', 
         dest_file_path="/work2/01837/jstubbs/stampede2/hello-tapis.pynb")
```
It's important to note that if you are using the Jupyter notebook, the `/some/local/file.txt` path is relative to the Jupyter notebook path itself. As such, you can check the path of the notebook through the `pwd` command and can create a dummy script to test the upload Tapis service. 


And we should now see our file when we do another listing:
```python
# check that file is now there:
t.files.listFiles(systemId='stampede2.jstubbs', 
                  path="/work2/01837/jstubbs/stampede2/hello-tapis.ipynb")
```
The output confirms the presence of the file:
```
[
 group: 814212
 lastModified: 2021-12-02T00:12:54Z
 mimeType: None
 name: hello-tapis.ipynb
 nativePermissions: rw-------
 owner: 811324
 path: /work2/01837/jstubbs/stampede2/hello-tapis.ipynb
 size: 40469
 type: file
 url: tapis://stampede2.jstubbs-2/work2/01837/jstubbs/stampede2/hello-tapis.ipynb]
 ```

## Downloading Files
Finally, we can download a file using the syntax:
```python
t.files.getContents(system_id=<system_id>, 
                    path='/some/remote/file.txt')
```

For example,
```python
t.files.getContents(system_id='stampede2.jstubbs-2', 
                    path="/work2/01837/jstubbs/stampede2/hello-tapis.ipynb")
```
Note that the function returns the file contents as a raw bytes object.
