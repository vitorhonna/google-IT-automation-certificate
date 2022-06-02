#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

echo $files

for file in $files; do
        filename="/home/student-00-be74dce8b516$file"
        if [ -f $filename ]; then
                echo $filename >> oldFiles.txt
        fi
done