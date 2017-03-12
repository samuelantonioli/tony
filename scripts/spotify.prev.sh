#!/bin/bash

WID=$(xdotool search spotify | head -n1)
xdotool windowactivate $WID
sleep 0.5
# prev song:
xdotool mousemove 1090 490 click 1
sleep 0.9
xdotool click 1
