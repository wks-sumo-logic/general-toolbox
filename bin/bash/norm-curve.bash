#!/usr/bin/env bash
umask 022

length=$1
for (( i = 0; i < length ; i++ ))
do
	echo $((1 + RANDOM % length))
done
