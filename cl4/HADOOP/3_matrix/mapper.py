#!/usr/bin/env python3
import sys

# Reading the input from stdin
for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')

    tag = parts[0]  # 'A' or 'B'
    i = int(parts[1])
    j = int(parts[2])
    value = float(parts[3])

    if tag == 'A':
        # For Matrix A, we emit (i, j), ('A', k, value) for all j in B
        for k in range(2):  # You can set this based on the number of columns in B
            print(f"{i},{k}\tA,{j},{value}")
    elif tag == 'B':
        # For Matrix B, we emit (i, j), ('B', k, value) for all i in A
        for k in range(2):  # You can set this based on the number of rows in A
            print(f"{k},{j}\tB,{i},{value}")
