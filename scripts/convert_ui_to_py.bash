#!/bin/bash
cd ../
input_folder=qt_templates/
output_folder=frontend/
for file in ${input_folder}*; do  pyuic5 -x ${file} -o "${file%.*}.py"; mv "${file%.*}.py" "${output_folder}" ;done
