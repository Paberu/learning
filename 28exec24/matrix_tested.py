def MatrixTurn(matrix, m, n, t):
    for i in range(m):
        matrix[i] = list(matrix[i])

    for _ in range(t):
        for deep in range(min(m, n)//2):
            temp = matrix[deep][n-1-deep]
            temp2 = matrix[m-1-deep][n-1-deep]
            temp3 = matrix[m-1-deep][deep]

            for i in reversed(range(deep, n-deep)):
                if i > deep:
                    matrix[deep][i] = matrix[deep][i-1]

            for j in reversed(range(deep, m-deep)):
                if j > deep:
                    matrix[j][n-1-deep] = matrix[j-1][n-1-deep]
            matrix[deep+1][n-1-deep] = temp

            for i in range(deep, n-1-deep):
                matrix[m-1-deep][i] = matrix[m-1-deep][i+1]
            matrix[m-1-deep][n-2-deep] = temp2

            for j in range(deep, m-1-deep):
                matrix[j][deep] = matrix[j+1][deep]
            matrix[m-2-deep][deep] = temp3

    for i in range(m):
        matrix[i] = ''.join(matrix[i])

matr = ['123456','234567','345678','456789']

MatrixTurn(matr,4,6,1)

for i in range(4):
    print(matr[i])
