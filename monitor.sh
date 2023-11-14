#!/usr/bin/bash

prev_content=""

while true; do
  #content=$(wl-paste)
  content=$(paste)

  if [[ "$content" != "$prev_content" ]]; then
    prev_content="$content"
    python /home/dakai/Apps/taobao-link-converter/convert.py
  fi

  sleep 1
done
