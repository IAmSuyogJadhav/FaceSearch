# FaceSearch
       █▀▀ █▀▀█ █▀▀ █▀▀   █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █  █       
       █▀▀ █▄▄█ █   █▀▀   ▀▀█ █▀▀ █▄▄█ █▄▄▀ █   █▀▀█       
       ▀   ▀  ▀ ▀▀▀ ▀▀▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀ ▀  ▀       

FaceSearch: Searches for faces in a given image using the Google Reverse Image Search engine.

## Installation
First clone this repo. Now, to install the dependencies and create the alias for FaceSearch, run the `install.sh`.
``` bash
bash install.sh
```
## Usage
Once it finishes, you can now use the following command on the terminal to detect and search for the faces in any image.
``` bash
facesearch path/to/Image
```
## Examples
Test image:

![alt text](./example/test.jpg "Test image")

On command line:
``` bash
anon@anon-pc:~/FaceSearch$ facesearch example/test.jpg
[ INFO:0] Initialize OpenCL runtime...
---------------------------------------------------------------------
On the next screen, note the number for the face you want to search.
---------------------------------------------------------------------
Press any key to continue...

Input the face number:
1
Uploading image..
Thanks for using this tool! Please report any bugs to github.
anon@anon-pc:~/FaceSearch$ Created new window in existing browser session.
█
```
Window:

![alt text](./example/test0.png "The output window")

In the browser:

![alt text](./example/test1.png "Browser output")

Any feedback, bug reports and issues are welcome!

Image Source: [Rediff](http://im.rediff.com/getahead/2018/feb/26tanmay1.jpg)
