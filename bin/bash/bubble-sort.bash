#!/usr/bin/env bash
umask 022
set -e
Input=$*
IFS=' ' read -r -a InputArray <<< "${Input}"

### echo "Array in original order"
### echo "${InputArray[*]}" 
  
# Performing Bubble sort  
length=${#InputArray[@]}

BubbleSort(){
	for (( i = 0; i < length ; i++ ))
	do
		for (( j = i; j < length; j++ ))
		do
			if [ "${InputArray[$i]}" -gt "${InputArray[$j]}"  ]; then
				TempValue=${InputArray[$i]}
				InputArray[$i]=${InputArray[$j]}
				InputArray[$j]=$TempValue
			fi
		done
	done
}

ArrayReport(){
	Label="${1:-"Unsorted"}"
	echo "$Label Array Numbers Are:"
	for (( i = 0; i < length; i++ ))
	do
		echo "$Label :: ${InputArray[$i]}"
	done
}

ArrayReport ## "Unsorted"
BubbleSort
ArrayReport "Ordered"
