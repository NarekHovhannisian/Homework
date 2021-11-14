def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    for row in range(rows):
        for column in range(columns):
            new_matrix[column][row] = matrix[row][column]
    return new_matrix
