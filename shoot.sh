#!/bin/bash
echo "don't forget to: source activate aind"
/bin/zsh -i -c 'chrome https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/f719d723-7ee0-472c-80c1-663f02de94f3/lessons/222105c1-630c-4726-a162-8e3380a4b67d/project'
atom .
pandoc heuristics.md --listings -H markdown-pdf.tex --latex-engine=xelatex -o heuristic_analysis.pdf
pandoc research_review.md --latex-engine=xelatex -o research_review.pdf
