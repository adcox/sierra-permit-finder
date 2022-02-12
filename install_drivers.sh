#!/bin/sh

if [ "$#" -gt 0 ] && [ -d "$1" ]; then
    INSTALL=$1
else
    INSTALL="$HOME/.local"
fi
echo "Set install location to $INSTALL"

if [ ! -f "$INSTALL/bin/geckodriver" ]; then
    echo "Installing geckodriver"

    mkdir temp
    cd temp

    # TODO - this is a linux-specific version; query for OS and download
    # the right now; also cater install location to the OS
    wget 'https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz'

    tar -zxvf geckodriver-*
    mv geckodriver "$INSTALL/bin/"
    cd ..
    rm -rf temp
else
    echo "geckodriver already installed; done!"
fi
