#!/bin/bash

echo "Getting all channels ...";

html=`somafm_get_html.sh | grep "TEMPORARY-FILE" | awk '{print $2}'`;
somafm_parse_html.sh ${html} | xargs somafm_get_channels.sh;
rm ${html};

echo " ... Done!";
