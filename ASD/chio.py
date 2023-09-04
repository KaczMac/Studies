#skończone
#Maciej Kaczmarski, 410587
class Matrix:
    def __init__(self, mat, val: int = 0):
        if isinstance(mat,tuple):
            b = []
            for i in range(mat[0]):
                a = [val] * mat[1]
                b.append(a)
            self._matrix = b
        else:
            self._matrix = mat
    def __add__(self, sec_matrix):
        if self.size() != sec_matrix.size():
            raise ValueError
        else:
            mat = self._matrix
            res = [[0 for i in range(self.size()[1])] for j in range(self.size()[0])]
            for row in range(self.size()[0]):
                for col in range(self.size()[1]):
                    res[row][col] = mat[row][col] + sec_matrix[row][col]
            res = Matrix(mat)
            return res
    def __mul__(self, sec_matrix):
        if self.size()[1] != sec_matrix.size()[0]:
            raise ValueError
        else:
            row = self.size()[0]
            col = sec_matrix.size()[1]
            multiplied = [[0 for i in range(col)] for j in range(row)]
            for i in range(row):
                for j in range(col):
                    for k in range(self.size()[1]):
                        multiplied[i][j] += self._matrix[i][k] * sec_matrix[k][j]
            res = Matrix(multiplied)
            return res
    def __getitem__(self,item):
        return self._matrix[item]
    def  __str__(self):
        s = ''
        for i in range(self.size()[0]):
            s += '|'
            for j in range(self.size()[1]):
                s += '{:2d} '.format(self._matrix[i][j])
            s += '|\n'
        return s
    def size(self) -> tuple:
        return len(self._matrix), len(self._matrix[0])


def transpose(matrix: Matrix):
    size = matrix.size()
    row = size[0]
    col = size[1]
    transposed = [[0 for i in range(row)] for j in range(col)]
    for i in range(row):
        for j in range(col):
            transposed[j][i] = matrix[i][j]
    res = Matrix(transposed)
    return res

matrix1 = Matrix([[1, 0, 2], [-1, 3, 1]])

matrix2 = Matrix((2, 3), 1)

matrix3 = Matrix([[3, 1], [2, 1], [1, 0]])

matrix_T = transpose(matrix1)
print(matrix_T)
matrix4 = matrix1 + matrix2
print(matrix4)
matrix5 = matrix1 * matrix3
print(matrix5)


def chio(matrix: Matrix):
    if matrix.size()[0] == matrix.size()[1] and matrix.size()[0] > 2:
        factor = 1/(matrix[0][0]**2)
        result = [[0 for i in range(matrix.size()[0])]for j in range(matrix.size()[1])]
        for i in range(matrix.size()[0]):
            for j in range(matrix.size()[1]):
                result[i][j] = chio(Matrix([[matrix[0][0],matrix[i][0]],[matrix[0][j],matrix[i][j]]]))
        return factor*chio(Matrix(result))
    elif matrix.size()[0] == matrix.size()[1] and matrix.size()[0] == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    

print(chio(Matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])))