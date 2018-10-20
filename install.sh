#!/bin/bash
echo "Installing Python3.6"
sudo apt-get install python3.6
sudo apt-get install build-essential
sudo apt-get install python3-pip

echo "Installing OpenCV and NumPy..."
pip3 install NumPy opencv-python

echo "Installing FaceSearch..."
cp .facesearch ~ -r

# Remove existing aliases, if any
while grep -qE "alias facesearch=\"python.+" ~/.bash_aliases
do grep -vE "alias facesearch=\"python.+" ~/.bash_aliases > temp && mv -f temp ~/.bash_aliases
done

echo "alias facesearch=\"python3 ~/.facesearch/facesearch.py ~/.facesearch/face_alt.xml\"" >> ~/.bash_aliases
. ~/.bashrc

echo "All set!"
echo "Now Just use facesearch path/to/image to use FaceSearch!"
