class Matrix:
    def __init__(self, matrix, par=0):
        if isinstance(matrix, tuple):
            self.matrix = [[par for _ in range(matrix[1])] for _ in range(matrix[0])]
        else:
            self.matrix = matrix

    def __len__(self):
        return len(self.matrix)

    def getitem(self, key):
        if key >= len(self.matrix):
            return None
        else:
            return self.matrix[key]

    def __add__(self, matrix2):
        if len(self.matrix) == len(matrix2) and len(self.matrix[0]) == len(matrix2[0]):
            matrix3 = Matrix((len(self.matrix), len(self.matrix[0])))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    matrix3[i][j] = self.matrix[i][j] + matrix2[i][j]
            return matrix3
        else:
            return None

    def __mul__(self, matrix2):
        if len(self.matrix) == len(matrix2[0]) and len(self.matrix[0]) == len(matrix2):
            matrix3 = Matrix((len(self.matrix), len(matrix2[0])))
            for i in range(len(self.matrix)):
                for j in range(len(matrix2[0])):
                    for k in range(len(self.matrix[0])):
                        matrix3[i][j] += self.matrix[i][k] * matrix2[k][j]
            return matrix3
        else:
            return None

    def __str__(self):
        return '\n'.join(str(elem) for elem in self.matrix)

def transpose_matrix(matrix):
    t_matrix = Matrix((len(matrix[0]), len(matrix)))
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            t_matrix[i][j] = matrix[j][i]
    return t_matrix
