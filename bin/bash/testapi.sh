#!/usr/bin/env bash
umask 022
export PATH="/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:$PATH"
webcmd="curl -s"
action="-X GET"

mycred="-u <APIKEY>:<APISECRET>"
endpoint="<ENDPOINT>"
target="https://api.${endpoint}.sumologic.com/api"

declare -A objectlist
objectlist[user]="v1/users"
objectlist[roles]="v1/roles"
objectlist[collectors]="v1/collectors"
objectlist[content]="v1/content"
objectlist[connections]="v1/connections"
objectlist[extractRules]="v1/extractionRules"

for key in "${!objectlist[@]}";
do
    echo "### Retrieving Key: $key"
    value=${objectlist[$key]}
    echo "$webcmd $mycred $action $target/$value | jq '.' "
done
