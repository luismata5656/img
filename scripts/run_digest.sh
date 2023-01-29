#!/bin/bash

for d in resize/*; do
    for file in "$d"/*
    do
        python3 __init__.py "$file"
    done
done

