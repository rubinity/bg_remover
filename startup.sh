#!/bin/bash

# ensure symlink exists
if [ ! -e /usr/src/app/src/U2Net/saved_models/u2net/u2net.pth ]; then
    ln -s /model/u2net.pth /usr/src/app/src/U2Net/saved_models/u2net/u2net.pth
fi

exec "$@"
