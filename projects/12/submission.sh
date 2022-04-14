#!/bin/bash

rm -rf submission
mkdir submission
zip project12.zip Array.jack Keyboard.jack Math.jack Memory.jack Output.jack Screen.jack String.jack Sys.jack
mv project12.zip submission

git add -A
git commit -m "Project 12"
git push