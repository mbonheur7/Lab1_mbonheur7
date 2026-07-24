#!/usr/bin/python3
if [! -d "archive" ]; then
    mkdir archive
fi

timestamp = $(date +"%Y%m%d-%H%M%S")
archived_name="grades_${timestamp}.csv"

mv grades.csv "archive/${archived_name}"

touch grades.csv

echo "[$timestamp] Archived '$archived_name' from grades.csv" >> organizer.log
echo "Done. Archuved to archive/${archived_name} and logged."
