# Python File Writer

This repository contains a command line code writer. Its syntax is
specified for Python.

It is meant for the fast writing of little python scripts without the need
an IDE large code editor started.

The File Writer is currently in initial development and has not yet got a 
stable version.

---
## Example

```
D:\>py -m writer myfile    
========== myfile.py ==========

for i in range(10):
    print("hello world!")
    
print("hello python")


================================ 
Saved successfully

D:\>
```
---

## Goals

The Writer shall have the fastest usable syntax to be a useful
alternative to editors. Therefor, there are some restrictions:

* Three empty lines inserted end the editor and save the script
* A `:` causes an indent for the following lines
* If a script is indented at the current position, a blank line  causes a dedention of the following lines

---
## Developments

* More options
* Exception handling
* four spaces cause an indent