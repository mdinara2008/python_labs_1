def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []

    for row in mat:
        if not isinstance(row,list):
            raise ValueError('матрица должна быть списком списков')
        if len(row) != len(mat[0]):
            raise ValueError('рваная матрица')
    
    stroka = len(mat)
    stolb = len(mat[0])
    res = []
    
    for j in range(stolb):
        res.append([])

    for i in range(stroka):
        for j in range(stolb):
            res[j].append(mat[i][j])
    return res
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))



def row_sums(mat: list[list[float | int]]) -> list[float]:
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError('рваная матрица')
        
    res = []
    for row in mat:
        res.append(sum(row))
    return res
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))


def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in mat:
        if len(i)!=len(mat[0]):
            raise ValueError('рваная матрица')

    res = []
    col_num = len(mat[0])
    for j in range(col_num): #по столбцам
        col_sum = 0
        for i in range(len(mat)): #по строкам
            col_sum += mat[i][j]
        res.append(col_sum)
    return res
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))