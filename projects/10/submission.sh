#!/bin/bash

rm -rf submission
mkdir submission
cd jack_compiler
zip project10.zip JackAnalyzer.py jack_tokenizer.py compilation_engine.py lang.txt
cd ..
mv jack_compiler/project10.zip submission

git add -A
git commit -m "Project 10"
git push