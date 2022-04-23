#!/usr/bin/env bash

#
### Basic Tasks. Serially Executed
#

umask 022

sleeptime='1'

export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:$PATH"

execute_task() {
   sleep ${sleeptime}
   echo "TASK: $1"
}

for my_task in {a..z}; do 

   execute_task "$my_task"

done
