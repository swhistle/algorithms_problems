def generate_pascals_triangle(numRows: int) -> list:
    if numRows < 1 or numRows > 30:
        return []

    pascals_triangle = [[1]]

    for i in range(2, numRows + 1):
        previous_row = pascals_triangle[-1]
        next_row = [1] * (len(previous_row) + 1)

        for j in range(0, len(next_row)):
            if j != 0 and j != len(next_row) - 1: # all elements except first and last
                next_row[j] = previous_row[j] + previous_row[j - 1]

        pascals_triangle.append(next_row)

    return pascals_triangle


pascals_triangle_1 = generate_pascals_triangle(1)
print(pascals_triangle_1)

pascals_triangle_2 = generate_pascals_triangle(2)
print(pascals_triangle_2)

pascals_triangle_3 = generate_pascals_triangle(3)
print(pascals_triangle_3)

pascals_triangle_4 = generate_pascals_triangle(4)
print(pascals_triangle_4)

pascals_triangle_5 = generate_pascals_triangle(5)
print(pascals_triangle_5)


