#!/bin/bash

cat styleList.txt | while read LINE;
do
	echo "$LINE";
	python3 addCSS.py "$LINE";
done
