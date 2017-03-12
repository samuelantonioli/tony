#!/bin/bash

# http://stackoverflow.com/a/42131272
A="$(python -c "import urllib.parse;print(urllib.parse.quote(input()))" <<< "$@")"

(chromium --incognito "https://www.google.de/search?q=$A" &> /dev/null &)
sleep 3
# https://github.com/koldkaching/semicomplete/issues/66#issuecomment-227793797
WID=$(xdotool search --desktop 0 chromium | head -n1)
xdotool windowactivate $WID
