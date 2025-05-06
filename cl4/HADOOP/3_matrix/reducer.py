#!/usr/bin/env python3
import sys
from collections import defaultdict

# Variables to store the values from A and B matrices for a given key (i, j)
current_key = None
A_vals = defaultdict(float)
B_vals = defaultdict(float)

def emit_product(i_k, A_vals, B_vals):
    total = 0
    for k in range(2):  # You can set this based on the number of columns/rows
        total += A_vals.get(k, 0) * B_vals.get(k, 0)
    if total != 0:
        print(f"{i_k}\t{total}")

# Reading the input from stdin
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    
    # Extracting the i, j part of the key and values
    i, j = map(int, key.split(','))
    parts = value.split(',')
    tag = parts[0]
    k = int(parts[1])
    val = float(parts[2])

    # Grouping the values by (i, j)
    if current_key != (i, j) and current_key is not None:
        # Emit the computed result for the previous key
        emit_product(current_key, A_vals, B_vals)
        # Reset for the next key
        A_vals.clear()
        B_vals.clear()

    current_key = (i, j)

    if tag == 'A':
        A_vals[k] = val
    elif tag == 'B':
        B_vals[k] = val

# Emit the last key
if current_key:
    emit_product(current_key, A_vals, B_vals)
