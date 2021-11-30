# Managing Data on a System

Now that we have a system created and a credential registered, we can now start using Tapis
to do some "real" work. In this short tutorial, we will use the Files API to get a file 
listing on a directory, upload a file to the directory, and download a file.

## Listing Files in a Directory
To list files on a path, use the `listFiles()` endpoint of the `files` service, like so:

```python
t.files.listFiles(systemId='<system_id>', path="/some/path")
```
replacing `<system_id>` with the system id and `/some/path` with the path on the system
you want to list. Note that `/some/path` is relative to the `rootDir` of the system; that
is, Tapis will prepend the `rootDir` path defined for the system to the `path` you 
provide.

For example, to list files on our Stampede2 system, we could use a call like this:
```python
t.files.listFiles(systemId='stampede2.jstubbs', path="/work/01837/jstubbs/stampede2")
```