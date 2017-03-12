#!/bin/bash

# http://stackoverflow.com/a/42131272
A="$(python -c "import urllib.parse;print(urllib.parse.quote(input()))" <<< "$@")"

(chromium --incognito "https://www.youtube.com/results?search_query=$A" &> /dev/null &)
sleep 3
# https://github.com/koldkaching/semicomplete/issues/66#issuecomment-227793797
WID=$(xdotool search --desktop 0 chromium | head -n1)
xdotool windowactivate $WID
sleep 0.5
xdotool key ctrl+l
xdotool type 'javascript:'
xdotool type "try{document.getElementsByClassName('.pyv-afc-ads-container')[0].innerHTML=''}catch(e){};document.querySelector('.yt-lockup-video .yt-uix-tile-link').click();"
xdotool key Return
