#############################################################
#       █▀▀ █▀▀█ █▀▀ █▀▀   █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █  █       #
#       █▀▀ █▄▄█ █   █▀▀   ▀▀█ █▀▀ █▄▄█ █▄▄▀ █   █▀▀█       #
#       ▀   ▀  ▀ ▀▀▀ ▀▀▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀ ▀  ▀       #
#############################################################
# FaceSearch: Search for faces in a given image using       #
# Google Reverse Image Search                               #
# ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ #
# File name: search.py                                      #
# Author: Suyog Jadhav (https://github.com/IAmSuyogJadhav)  #
# Date created: 10 Jul 2018                                 #
# Date last modified: 10 Jul 2018                           #
# Python Version: 3.6                                       #
# ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ #
# Fork me on: https://github.com/IAmSuyogJadhav/FaceSearch  #
#############################################################
"""
The helper script for FaceSearch.
"""

import requests
import webbrowser
import sys


def grab(faces):
    """
    Takes as input all the faces and requests reponse from the user.
    Params:
        faces: A python list of NumPy arrays
    Returns: response, an integer
    """

    try:
        response = int(input())
        faces[response]
    except ValueError:
        print('Enter a valid integer. Try again.')
        grab()
    except IndexError:
        print('Enter a valid integer within %d to %d. Try again.' %
              (0, len(faces) - 1))
        grab()
    return response


def Search():
    """
    Uploads the _search_.jpg file to Google and searches for it using Google
    Reverse Image Search.
    """
    filePath = '~/_search_.jpg'
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {
        'encoded_image': (filePath, open(filePath, 'rb')),
        'image_content': ''}

    print("Uploading image..")
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    webbrowser.open(fetchUrl)
    print("Thanks for using this tool! Please report any bugs to github.")
    sys.exit()
