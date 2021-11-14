def matrixReshape(mat, r, c):
    result = [[None for _ in range(c)] for _ in range(r)]
    mat_arr = []
    for arr in mat:
        mat_arr += arr
    if len(mat_arr) != r*c:
        return mat
    for i in range(r):
        for j in range(c):
            result[i][j] = mat_arr[i * c + j]
    return result
