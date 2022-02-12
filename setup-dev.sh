#!/bin/sh

if [ "$?VIRTUAL_ENV" ]; then
    INSTALL="$VIRTUAL_ENV"
else
    INSTALL="$HOME/.local"
fi

pip install .

# Make the lib installation of sierra_permits a symlink so that changes to
# the local files are seen
rm -rf "$INSTALL/lib/python3.8/site-packages/sierra_permits"
ln -s "`pwd`/sierra_permits" "$INSTALL/lib/python3.8/site-packages/sierra_permits"

./install_drivers.sh "$INSTALL"

