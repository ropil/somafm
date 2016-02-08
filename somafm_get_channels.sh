#!/bin/bash

if [ -z $1 ]; then
  echo "USAGE: $0 <channel1> [<channel2> [...]]";
fi;

channels=$*
somafm="http://somafm.com/"
filetype=".pls"

for channel in $channels; do
  wget ${somafm}${channel}${filetype};
done;
