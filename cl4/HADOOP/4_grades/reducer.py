#!/usr/bin/env python3
import sys
from collections import defaultdict

# Grading function to assign grades based on the total marks
def assign_grade(total):
    if total >= 180:
        return 'A'
    elif total >= 150:
        return 'B'
    elif total >= 120:
        return 'C'
    elif total >= 100:
        return 'D'
    else:
        return 'F'

# Reducer function to accumulate marks and assign grades
def reducer():
    current_student = None
    total_marks = 0

    # Read input from stdin (from Hadoop)
    for line in sys.stdin:
        line = line.strip()
        student, mark = line.split('\t')  # Split by tab (output from the mapper)
        mark = int(mark)

        if current_student == student:
            # If the student is the same as the previous, accumulate the marks
            total_marks += mark
        else:
            if current_student:
                # When the student changes, print the result for the previous student
                print(f"{current_student}\t{total_marks}\t{assign_grade(total_marks)}")
            # Update to the new student
            current_student = student
            total_marks = mark

    # Print the result for the last student
    if current_student == student:
        print(f"{current_student}\t{total_marks}\t{assign_grade(total_marks)}")

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    reducer()
