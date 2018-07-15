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
**Also**, note that the `path/to/Image` can be an internet URL as well! (prefixed with http: or https:)
So, you can just drag an image off the internet over the terminal to get its URL pasted over there and search for faces in it using FaceSearch. Really convenient.

## Examples
Test image:

![alt text](./example/test.jpg "Test image")

On command line:
``` bash
anon@anon-pc:~/FaceSearch$ facesearch example/test.jpg
[ INFO:0] Initialize OpenCL runtime...
Uploading image..
Thanks for using this tool! Please report any issues to github.
https://github.com/IAmSuyogJadhav/FaceSearch/issues
anon@anon-pc:~/FaceSearch$ Created new window in existing browser session.
█
```
Window:

![alt text](./example/test0.png "The output window")

In the browser:

![alt text](./example/test1.png "Browser output")

Any feedback, bug reports and issues are welcome!

Image Source: [Rediff](http://im.rediff.com/getahead/2018/feb/26tanmay1.jpg)
