# -*- coding: utf-8 -*-
#############################################################
#       █▀▀ █▀▀█ █▀▀ █▀▀   █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀ █  █       #
#       █▀▀ █▄▄█ █   █▀▀   ▀▀█ █▀▀ █▄▄█ █▄▄▀ █   █▀▀█       #
#       ▀   ▀  ▀ ▀▀▀ ▀▀▀   ▀▀▀ ▀▀▀ ▀  ▀ ▀ ▀▀ ▀▀▀ ▀  ▀       #
#############################################################
# FaceSearch: Searches for faces in a given image using     #
# Google Reverse Image Search engine                        #
# ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ #
# File name: facesearch.py                                  #
# Author: Suyog Jadhav (https://github.com/IAmSuyogJadhav)  #
# Date created: 10 Jul 2018                                 #
# Date last modified: 10 Jul 2018                           #
# Python Version: 3.6                                       #
# ▀ ▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ ▀ ▀ ▀ #
# Fork me on: https://github.com/IAmSuyogJadhav/FaceSearch  #
#############################################################

import numpy as np
import cv2
import sys
import requests
import webbrowser
import os


def Search():
    """
    Uploads the _search_.jpg file to Google and searches for it using Google
    Reverse Image Search.
    """
    filePath = '_search_.png'
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {
        'encoded_image': (filePath, open(filePath, 'rb')),
        'image_content': ''}

    print("Uploading image..")
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    webbrowser.open(fetchUrl)
    print("Thanks for using this tool! Please report any issues to github."
          "\nhttps://github.com/IAmSuyogJadhav/FaceSearch/issues")
    os.remove('_search_.png')


def handle_click(event, x, y, flags, params):
    """
    Records clicks on the image and lets the user choose one of the detected
    faces by simply pointing and clicking.
    """
    # Capture when the LClick is released
    if event == cv2.EVENT_LBUTTONUP and y > a // 2:  # Ignore clicks on padding
        response = x // (faces_copy.shape[1] // len(faces))
        cv2.destroyAllWindows()
        cv2.imwrite('_search_.png', faces[response])
        try:
            Search()
        except KeyboardInterrupt:  # Delete the generated image if user stops
            print("\nTerminated execution. Cleaning up...")  # the execution.
            os.remove('_search_.png')
        sys.exit()


# The path to the face detection Haar cascade. Specified in the install.sh file
cascade = sys.argv[1]

try:
    path = sys.argv[2]
except IndexError:  # Check if any path is entered or not.
    print("Please input a path.\nUsage: python search.py path/to/file")
    sys.exit()

image = cv2.imread(path)
if image is None:  # Check if the path is valid.
    print("""Image could not be loaded.
    1. Make sure you typed in the path to the image correctly.
    2. Make sure you have read permissions to the image file.""")
    sys.exit()

cascade = cv2.CascadeClassifier(cascade)  # Load the CascadeClassifier
detected = cascade.detectMultiScale(image)  # Detect faces
faces = []

for x, y, w, h in detected:
    faces.append(image[y:y+h, x:x+w, :])  # Crop out individual faces

if len(faces) == 0:  # If no face is detected in the image.
    print("No face detected.")
    sys.exit()

faces_copy = faces.copy()

a = 128  # To resize all faces to square of side a. Only for displaying.
for i, face in enumerate(faces_copy):  # Prepare for displaying.
    faces_copy[i] = cv2.resize(face, (a, a))  # Resize faces
    faces_copy[i] = np.pad(  # Pad the faces with a white border
            faces_copy[i], ((2, 2), (2, 2), (0, 0)),
            mode='constant', constant_values=((255, 255), (255, 255), (0, 0))
            )
    cv2.circle(  # Draw a quarter-circle at bottom-left of image.
            faces_copy[i], (5, a), int(0.25*a), (0, 200, 0), -1
            )
    cv2.putText(  # Type the index of the face over the quarter circle.
            faces_copy[i], str(i), (0, a), cv2.FONT_HERSHEY_DUPLEX,
            0.007*a, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA
            )

faces_copy = np.hstack(tuple(faces_copy))  # For creating a single strip

if faces_copy.shape[1] < 4 * a:
    pad = 4 * a - faces_copy.shape[1]
    faces_copy = np.pad(
            faces_copy, ((0, 0), (pad // 2, pad // 2), (0, 0)),
            mode='constant', constant_values=((0, 0), (255, 255), (0, 0))
            )


faces_copy = np.pad(  # Padding above to write some text.
        faces_copy, ((a//2, 0), (0, 0), (0, 0)),
        mode='constant', constant_values=((255, 255), (0, 0), (0, 0))
        )

cv2.putText(  # Writing some text on the top padded portion.
        faces_copy,
        # 'Note the number of the face to search.', (5, a // 4),
        'Click on the face you want to search for.', (5, a // 4),
        cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 200, 0), lineType=cv2.LINE_AA
        )

cv2.namedWindow('Choose the face')
cv2.setMouseCallback('Choose the face', handle_click)
cv2.imshow('Choose the face', faces_copy)
cv2.waitKey(0)
