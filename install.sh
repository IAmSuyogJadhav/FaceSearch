#!/bin/bash
echo "Installing OpenCV and NumPy..."
pip install NumPy opencv-python

echo "Installing FaceSearch..."
cp .facesearch ~ -r
echo "alias facesearch=\"python ~/.facesearch/facesearch.py ~/.facesearch/face_alt.xml\"" >> ~/.bash_aliases
source ~/.bashrc
echo "All set!"
echo "Now Just use facesearch path/to/image to use FaceSearch!"
