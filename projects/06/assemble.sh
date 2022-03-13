#!/bin/bash

# Clean up old files
rm -rf submission

# Run the assembler
python3 assembler/hack_assembler.py add/Add.asm
python3 assembler/hack_assembler.py max/Max.asm
python3 assembler/hack_assembler.py rect/Rect.asm
python3 assembler/hack_assembler.py pong/Pong.asm

# Copy the output files to the current directory
mkdir submission
cp add/Add.hack submission
cp max/Max.hack submission
cp rect/Rect.hack submission
cp pong/Pong.hack submission

# Create a random prog.txt file
echo "Empty file" > submission/prog.txt

# Create project6.zip
zip submission/project6.zip submission/Add.hack submission/Max.hack submission/Rect.hack submission/Pong.hack submission/prog.txt