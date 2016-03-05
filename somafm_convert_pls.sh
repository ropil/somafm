#!/bin/bash

if [ -z $1 ]; then
  echo "USAGE: $0 <pls> [<pls> [...]]";
fi;

playlists=$*

for pls in ${playlists[@]}; do
  name=`basename ${pls} .pls`;
  somafm_pls2m3u.py -new ${pls} > somafm_${name}.m3u
done;
