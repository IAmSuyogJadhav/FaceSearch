#!/bin/bash
echo "Installing OpenCV, NumPy and Selenium"
pip install NumPy opencv-pytyhon selenium

echo "Installing jq..."
sudo apt install jq

echo "Installing geckodriver for mozilla..."

# Source: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51
install_dir="/usr/local/bin"
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
if [[ $(uname) == "Darwin" ]]; then
    url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("macos"))')
elif [[ $(uname) == "Linux" ]]; then
    url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
else
    echo "can't determine OS"
    exit 1
fi
curl -s -L "$url" | tar -xz
chmod +x geckodriver
sudo mv geckodriver "$install_dir"
echo "Installed geckodriver binary in $install_dir"

cp .facesearch ~ -r
echo "alias facesearch=\"python ~/.facesearch/facesearch.py ~/.facesearch/face_alt.xml\"" >> ~/.bash_aliases
source ~/.bashrc
echo "All set!"
echo "Now Just use facesearch path/to/image to use FaceSearch!"
