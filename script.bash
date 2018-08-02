#!/bin/bash

cat latexFiles.txt | while read LINE;
do
	echo "$LINE";
	fileHTML="${LINE%%tex}html";
	pandoc "$LINE" -s --mathjax -o "$fileHTML"
done
