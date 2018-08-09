#!/bin/bash

cat latexFiles.txt | while read LINE;
do
	echo "$LINE";
	fileHTML="${LINE%%tex}html";
	python3 rewriteTex.py "$LINE";
	pandoc "${LINE%%.tex}_revised.tex" -s --mathjax -o "$fileHTML"
done
