#!/bin/bash

if [ ! -d "archive" ]; then
    mkdir archive
fi

if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv not found. Nothing to archive."
    exit 1
fi

timestamp=$(date +"%Y%m%d-%H%M%S")
archived_name="grades_${timestamp}.csv"
mv grades.csv "archive/${archived_name}"
touch grades.csv
echo "[$timestamp] Archived '$archived_name' from grades.csv" >> organizer.log
echo "Done. Archived to archive/${archived_name} and logged."
