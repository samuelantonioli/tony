#!/bin/bash

# https://github.com/koldkaching/semicomplete/issues/66#issuecomment-227793797
WID=$(xdotool search --desktop 0 chromium | head -n1)
xdotool windowactivate $WID
sleep 0.5
xdotool key ctrl+w
