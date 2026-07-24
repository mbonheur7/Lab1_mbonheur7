import csv
import sys
import os


def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)


def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")

    # a) Grade validation: every score must be between 0 and 100
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: '{item['assignment']}' has an invalid score ({item['score']}). Must be 0-100.")
            sys.exit(1)

    # b) Weight validation
    total_weight = sum(item['weight'] for item in data)
    formative_weight = sum(item['weight'] for item in data if item['group'] == 'Formative')
    summative_weight = sum(item['weight'] for item in data if item['group'] == 'Summative')

    if total_weight != 100:
        print(f"Error: Total weight is {total_weight}, expected 100.")
        sys.exit(1)
    if formative_weight != 60:
        print(f"Error: Formative weight is {formative_weight}, expected 60.")
        sys.exit(1)
    if summative_weight != 40:
        print(f"Error: Summative weight is {summative_weight}, expected 40.")
        sys.exit(1)

    # c) Final grade and GPA
    formative_total = sum(item['score'] * item['weight'] / 100 for item in data if item['group'] == 'Formative')
    summative_total = sum(item['score'] * item['weight'] / 100 for item in data if item['group'] == 'Summative')
    final_grade = formative_total + summative_total
    gpa = (final_grade / 100) * 5.0

    # d) Pass/Fail — 50% minimum in EACH category
    formative_pass = formative_total >= (60 / 2)
    summative_pass = summative_total >= (40 / 2)
    passed = formative_pass and summative_pass

    # e) Resubmission logic
    failed_formatives = [item for item in data if item['group'] == 'Formative' and item['score'] < 50]

    resubmission_list = []
    if failed_formatives:
        max_weight = max(item['weight'] for item in failed_formatives)
        resubmission_list = [item['assignment'] for item in failed_formatives if item['weight'] == max_weight]

    # f) Final output
    print(f"Formative Score: {formative_total:.2f} / 60")
    print(f"Summative Score: {summative_total:.2f} / 40")
    print(f"Final Grade: {final_grade:.2f} / 100")
    print(f"GPA: {gpa:.2f} / 5.0")
    print(f"Status: {'PASSED' if passed else 'FAILED'}")

    if resubmission_list:
        print("Eligible for resubmission:")
        for name in resubmission_list:
            print(f"  - {name}")
    else:
        print("No resubmission needed (or no failed Formative assignments).")


if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    # 2. Process the features
    evaluate_grades(course_data)