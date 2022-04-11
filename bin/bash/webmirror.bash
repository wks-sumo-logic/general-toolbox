#!/usr/bin/env bash

help_dir="help.sumologic.com"
help_url="https://${help_dir}"
sleep_time=5
wget_options="--no-verbose --mirror --convert-links --adjust-extension --page-requisites --no-parent"

###
### Expect this will take:
###
### 1) 2 hours
### 2) 1.5 Gbytes
### 3) moderate CPU impact
###
### 8,000 odd files
### 5,000 odd directories
###

echo ${help_url} | xargs -n 1 -P 4 wget ${wget_options}

###
### while 'true'; do du -sk ./$help_dir; sleep "${sleep_time}" ; done
###
