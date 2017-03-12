#!/bin/bash

WID=$(xdotool search spotify | head -n1)
xdotool windowactivate $WID
sleep 0.5
# next song:
xdotool mousemove 1230 490 click 1
