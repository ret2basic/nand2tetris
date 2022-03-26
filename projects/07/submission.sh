#!/bin/bash

rm -rf submission
mkdir submission
cd vm_translator
zip project7.zip code_writer.py lang.txt parser.py VMTranslator.py
cd ..
mv vm_translator/project7.zip submission

git add -A
git commit -m "Project 7"
git push