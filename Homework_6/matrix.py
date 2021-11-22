import numpy as np


class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])

    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0

    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)

    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'columns = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s

    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        """
        rows = [" ".join([str(self._matrix[i][j]) for j in range(self._columns)]) for i in range(self._rows)]
        matrix = "\n".join(rows)
        with open(filename, 'w') as f:
            f.write(matrix)

    def transpose(self):
        """
        Transpose the matrix.
        """
        t = Matrix(list=[[self._matrix[j][i] for j in range(self._rows)] for i in range(self._columns)])
        return t

    @property
    def shape(self):
        return self._columns, self._rows

    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        """
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                print("Shapes must be the same")
                return
            s = Matrix(list=[[self._matrix[i][j] + other._matrix[i][j] for j in range(self._columns)] for i in
                             range(self._rows)])
            return s
        return NotImplemented

    def __mul__(self, other):
        """
        The `*` operator. Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.

        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        """
        if isinstance(other, Matrix):
            if self.shape != other.shape:
                print("Shapes must be the same")
                return
            s = Matrix(list=[[self._matrix[i][j] * other._matrix[i][j] for j in range(self._columns)] for i in
                             range(self._rows)])
            return s
        if isinstance(other, (int, float)):
            s = Matrix(list=[[self._matrix[i][j] * other for j in range(self._columns)] for i in range(self._rows)])
            return s
        return NotImplemented

    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the first matrix must be equal to the number of rows in the second matrix.
        """
        if isinstance(other, Matrix):
            if self.shape[0] != other.shape[1]:
                print("The number of columns in the first matrix must be equal to the number of rows in the second "
                      "matrix.")
                return
            s = Matrix(list=[[0 for _ in range(other._columns)] for _ in range(self._rows)])
            for i in range(self._rows):
                for j in range(other._columns):
                    a = 0
                    for k in range(self._columns):
                        a += self._matrix[i][k] * other._matrix[k][j]
                    s._matrix[i][j] = a
            return s
        return NotImplemented

    @property
    def trace(self):
        """
        Find the trace of the matrix.
        """
        if self.shape[0] == self.shape[1]:
            s = 0
            for i in range(self._rows):
                s += self._matrix[i][i]
            return s
        print("Not a square matrix")
        return

    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        """
        if self.shape[0] == self.shape[1]:
            return np.linalg.det(self._matrix)
        print("Not a square matrix")
        return
