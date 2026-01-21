#!/bin/bash

# 5e
sed 's/^ *//' $1 | sed '/^$/d' > clean_$1
