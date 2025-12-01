import math

poly_values = [int(d) for d in input().split()]
n = int(math.log2(len(poly_values)))  # количество переменных

coefficients = []

triangle = [[0] * 2 ** n for i in range(2 ** n + 1)]

triangle[0] = poly_values

for i in range(1, 2 ** n):
    for j in range(2 ** n - i):
        triangle[i][j] = triangle[i - 1][j] ^ triangle[i - 1][j + 1]

for j in range(2 ** n):
    coefficients.append(triangle[j][0])
print(*coefficients)