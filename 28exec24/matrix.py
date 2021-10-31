def MatrixTurn(matrix, m, n, t):
    for i in range(len(matrix)):
        #matrix[i] = list(map(int, matrix[i]))
        matrix[i] = list(matrix[i])

    for deep in range():

    temp = matrix[0][n-1]
    for i in range(n-1, 0 ,-1):
        matrix[0][i] = matrix[0][i-1]

    temp2 = matrix[m-1][n-1]
    for j in range(m-1, 0, -1):
        matrix[j][n-1] = matrix[j-1][n- 1]
    matrix[1][n-1] = temp

    temp3 = matrix[m-1][0]
    for i in range(n-1):
        matrix[m-1][i] = matrix[m-1][i+1]
    matrix[m-1][n-2] = temp2

    temp4 = matrix[0][1]
    for j in range(m-1):
        matrix[j][0] = matrix[j+1][0]
    matrix[m-2][0] = temp3


matr = ["123456", "234567", "345678", "456789"]
for str in matr:
    print(list(str))
MatrixTurn(matr, 4, 6, 3)
for str in matr:
    print(str)