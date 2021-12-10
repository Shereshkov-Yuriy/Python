class Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))

    def __add__(self, other):
        try:
            matrix_sum = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))]
                          for i in range(len(self.matrix))]
            return Matrix(matrix_sum)
        except IndexError:
            return f'Размерность матриц должна быть одинаковой'


matrix_1 = [[35, 37, 33], [15, 19, 11], [24, 48, 86]]
matrix_2 = [[75, 73, 77], [95, 91, 99], [26, 68, 84]]
m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
print(m_1 + m_2)
