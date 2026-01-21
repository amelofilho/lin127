#!/bin/bash

sed 's/ /\n/g' $1 | sed '/^$/d'| tr -d '[:punct:][0-9]'| tr '[A-Z]' '[a-z]' |sort | uniq -c | sort -n > word_counts.txt

