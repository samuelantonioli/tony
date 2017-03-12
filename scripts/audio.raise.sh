#!/bin/bash
L="$1"
if [ -z "$L" ]; then
    L=1
fi
xdotool key --repeat $L XF86AudioRaiseVolume
