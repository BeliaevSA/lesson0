def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        return matrix
    for row in range(1, n + 1):
        values = []
        for colomn in range(1, m + 1):
            values.append(value)
        matrix.append(values)

    return matrix

result1 = get_matrix(n=2, m=2, value=10)
result2 = get_matrix(n=3, m=5, value=42)
result3 = get_matrix(n=4, m=2, value=13)
print(result1)
print(result2)
print(result3)