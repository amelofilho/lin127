#!/bin/bash

./clean_text.sh $1
# echo "created clean_$1"
./word_counts.sh clean_$1
# echo 'created word_counts.txt'
