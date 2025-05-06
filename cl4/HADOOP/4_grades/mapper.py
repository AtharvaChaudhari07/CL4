#!/usr/bin/env python3
import sys

# Mapper function to read input and output student name and marks
def mapper():
    for line in sys.stdin:
        line = line.strip()
        name, mark = line.split(',')
        print(f"{name}\t{mark}")

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    mapper()
