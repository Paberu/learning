import unittest


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


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.matr1 = ['123456','234567','345678','456789']

    def test_turning(self):
        MatrixTurn(self.matr1, 4, 6, 1)
        self.assertEqual(self.matr1, ['212345', '343456', '456767', '567898'])

unittest.main()
