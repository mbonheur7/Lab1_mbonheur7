# Grade Evaluator & Archiver

A Python application that evaluates a student's final academic standing from a CSV file of
course grades, paired with a Bash script that archives the grade data and resets the workspace.

## Files

## These are the files included
- `grade-evaluator.py` — reads grades from a CSV file, validates them, calculates GPA,
  determines pass/fail status, and flags assignments eligible for resubmission.
- `organizer.sh` — this is the archiver, it archives the curent `grades.csv` by adding a timestamp on the file turning it into a timestamped file inside an`archive/` folder, then  resets `grades.csv` to empty, and logs the action to `organizer.log`.
- `grades.csv` — this is the current batch of grade data (assignment, group, score, weight).

## Requirements

## we need
- Python 3
- Bash (Linux, or Git Bash / WSL on Windows)


## Running `grade-evaluator.py`

1. Make sure `grades.csv` is in the same folder as `grade-evaluator.py`.
2. Run the script:

python3 grade-evaluator.py
```
in your terminal.

3. When prompted, enter the filename `grades.csv`
4. The script should print:
   - The Formative and Summative scores
   - And the Final grade and GPA
   - The Pass/Fail status (requires ≥50% in both Formative and Summative categories)
   - Any Formative assignments eligible for resubmission (failed assignments with the
    highest weight among failures)

**Error handling:** if the file doesn't exist, or the weights don't add up correctly
(Total = 100, Formative = 60, Summative = 40), the script prints a clear error message and
exits instead of crashing.

 ## Running `organizer.sh`
 1. Make the script executable (only needs to be done once):

```bash
   chmod +x organizer.sh
```

2. Run it:

```bash
   ./organizer.sh
```

3. What it does:
   - Creates an `archive/` folder if one doesn't already exist
   - Renames the current `grades.csv` with a timestamp (e.g. `grades_20260724-153012.csv`)
     and moves it into `archive/`
   - Creates a fresh, empty `grades.csv` so the workspace is ready for the next batch
   - Appends a record of the action to `organizer.log`

If `grades.csv` doesn't exist when the script runs, it prints an error and exits without
making changes.

## Workflow

1. Add grade data to `grades.csv`.
2. Run `python3 grade-evaluator.py` to check the results.
3. Run `./organizer.sh` to archive that batch and reset for the next one.
