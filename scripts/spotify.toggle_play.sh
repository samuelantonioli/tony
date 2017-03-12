#!/bin/bash

WID=$(xdotool search spotify | head -n1)
xdotool windowactivate $WID
sleep 0.5
# play/pause song:
xdotool mousemove 1155 490 click 1
