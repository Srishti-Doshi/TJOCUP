# Write a program that:
# (a) Accepts an integer n followed by 2n lines as input.
# (b) Each of the first n lines contains a row of matrix A (comma-separated integers).
# (c) Each of the next n lines contains a row of matrix B (comma-separated integers).
# (d) Computes the matrix product AB.
# (e) Outputs the resulting matrix as n lines, with each line showing a row of the
# product as comma-separated integers.

n = int(input())
A = []; B = []

for i in range(n):
    row = input()
    row_list = [int(x) for x in row.split(",")]
    A.append(row_list)

for i in range(n):
    row = input()
    row_list = [int(x) for x in row.split(",")]
    B.append(row_list)

C = [[0 for j in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k]*B[i][k]

for row in C:
    print(",".join([str(x) for x in row]))