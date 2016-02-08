#!/bin/bash

somafm="http://somafm.com"
tmpfile=somafm_`date +%y%m%d%H%M`.html

wget ${somafm} -O ${tmpfile};
echo TEMPORARY-FILE ${tmpfile}
