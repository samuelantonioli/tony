#!/bin/bash

WID=$(xdotool search spotify | head -n1)
xdotool windowactivate $WID
sleep 0.5
# search
xdotool mousemove 125 450 click 1
sleep 0.3
xdotool mousemove 125 200 click 1
sleep 0.5
A="$@"
xdotool type "$A"
xdotool key Return
sleep 3
xdotool mousemove 390 290 click 1
#xdotool mousemove 415 290 click 1
