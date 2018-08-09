#!/bin/bash

cat htmlFiles.txt | while read LINE;
do
	echo "$LINE";
	python3 htmlAdd.py "$LINE";
done
