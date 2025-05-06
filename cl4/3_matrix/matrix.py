from collections import defaultdict

# Sample Matrices
A = [
    [1, 2, 3],   # 2x3 matrix
    [4, 5, 6]
]

B = [
    [7, 8],      # 3x2 matrix
    [9, 10],
    [11, 12]
]

# Get dimensions
num_rows_A = len(A)
num_cols_A = len(A[0])
num_rows_B = len(B)
num_cols_B = len(B[0])

assert num_cols_A == num_rows_B, "Incompatible matrix dimensions"

# Mapper
def mapper(A, B):
    mapped = []

    # Map A[i][k] → (i, j), ('A', k, value) for all j in B
    for i in range(num_rows_A):
        for k in range(num_cols_A):
            for j in range(num_cols_B):
                mapped.append(((i, j), ('A', k, A[i][k])))

    # Map B[k][j] → (i, j), ('B', k, value) for all i in A
    for k in range(num_rows_B):
        for j in range(num_cols_B):
            for i in range(num_rows_A):
                mapped.append(((i, j), ('B', k, B[k][j])))

    return mapped

# Reducer
def reducer(mapped_data):
    grouped = defaultdict(list)
    for key, value in mapped_data:
        grouped[key].append(value)

    result = defaultdict(int)
    for key, values in grouped.items():
        a_vals = {}
        b_vals = {}

        for tag, k, val in values:
            if tag == 'A':
                a_vals[k] = val
            elif tag == 'B':
                b_vals[k] = val

        # Compute dot product for key (i,j)
        total = 0
        for k in range(num_cols_A):  # or range(num_rows_B)
            total += a_vals.get(k, 0) * b_vals.get(k, 0)

        result[key] = total

    return result

# Run MapReduce
mapped_data = mapper(A, B)
reduced_result = reducer(mapped_data)

# Display Result Matrix C
print("Resultant Matrix C:")
C = [[0] * num_cols_B for _ in range(num_rows_A)]
for (i, j), val in reduced_result.items():
    C[i][j] = val

for row in C:
    print(row)
