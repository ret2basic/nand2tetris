#!/bin/bash

# Clean old files
rm -f Add.hack Max.hack Rect.hack Pong.hack prog.txt project6.zip

# Run the assembler
python3 hack_assembler.py add/Add.asm
python3 hack_assembler.py max/Max.asm
python3 hack_assembler.py rect/Rect.asm
python3 hack_assembler.py pong/Pong.asm

# Copy the output files to the current directory
cp add/Add.hack .
cp max/Max.hack .
cp rect/Rect.hack .
cp pong/Pong.hack .

# Create a random prog.txt file
echo "Empty file" > prog.txt

# Create project6.zip
zip project6.zip Add.hack Max.hack Rect.hack Pong.hack prog.txt