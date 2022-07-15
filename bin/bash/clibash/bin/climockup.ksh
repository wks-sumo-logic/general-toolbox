#!/usr/bin/env bash

umask 022
export PATH="/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:$PATH"
command=$( basename $( echo $0 ) ) 
cmdname=${command%%.*}

bindir=$( dirname $( realpath $0 ))
libdir=$( realpath $bindir/../lib )
verbdir=$( realpath $libdir/verbs )
objectsdir=$( realpath $libdir/objects )

declare -A apispecs
### apispecs["cse"]="https://api.sumologic.com/spec/sec"
apispecs["cip"]="https://api.sumologic.com/docs/sumologic-api.yaml"

for key in "${!apispecs[@]}"
do
  url=${apispecs[$key]}
  outputfile="/tmp/$key.json"
  [ -f $outputfile ] && rm -f $outputfile
  curl -s $url -o $outputfile
  cat /tmp/cip.json| yq -e '.. | select(. == "*") | (path | join(".")) '
done
