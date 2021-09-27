# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    matrix_array = []

    def __init__(self, matrix_array):
        self.matrix_array = matrix_array

    def __str__(self):
        matrix_str = ''
        for i in self.matrix_array:
            for j in i:
                next_numb = "%9.2f" % j
                matrix_str = matrix_str + next_numb
            matrix_str += '\n'
        return matrix_str

    def __add__(self, other):
        matrix_result = [[self.matrix_array[i][j] + other.matrix_array[i][j]
                          for j in range(0, len(self.matrix_array[i]))] for i in range(0, len(self.matrix_array))]
        return Matrix(matrix_result)


A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

B = [[2, 3, 1, 10],
    [-15, 7, 19, 1],
    [0, 3, 2, -10]]

matrix_A = Matrix(A)
matrix_B = Matrix(B)
matrix_C = matrix_A + matrix_B

print(matrix_A)
print(matrix_B)
print(matrix_C)
