#!/bin/bash

if [ -z $1 ]; then
  echo "USAGE: $0 <htmlfile>";
fi;

html=$1

grep -A 1 "li class=\"cbshort\"" $html | grep -o "href=\".*\"" \
  | awk -F \" '{print $2}'| awk -F / '{print $2}';
