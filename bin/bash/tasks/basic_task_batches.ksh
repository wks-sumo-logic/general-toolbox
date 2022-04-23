#!/usr/bin/env bash

#
### Basic Tasks. Serially Executed
#

umask 022

sleeptime=1
numworkers=3

export PATH="/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:$PATH"

execute_task() {
   sleep ${sleeptime}
   echo "PROCESSOR: $1 TASK: $2"

}

(
   for my_task in {a..z}; do

       ((counter=counter%numworkers)); ((counter++==0)) && wait
       execute_task "$counter" "$my_task" &

   done

)
