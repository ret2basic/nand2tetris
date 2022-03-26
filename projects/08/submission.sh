#!/bin/bash

rm -rf submission
mkdir submission
cd vm_translator
zip project8.zip code_writer.py lang.txt parser.py VMTranslator.py
cd ..
mv vm_translator/project8.zip submission

git add -A
git commit -m "Project 8"
git push