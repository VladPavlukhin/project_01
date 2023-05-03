# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

from sys import stdin


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d ' % i for i in row]) for row in self.matrix])
        # return '\n'.join([''.join([str(i)+' ' for i in row]) for row in self.matrix])

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, val):
        self.matrix[index] = val

    def __delitem__(self, index):
        del self.matrix[index]

    def __iter__(self):
        return self.matrix.__iter__()

    def __len__(self):
        return len(self.matrix)

    def __contains__(self, item):
        return item in self.matrix

    def __add__(self, other):
        assert type(other) is Matrix
        return Matrix([[e1 + e2 for e1, e2 in zip(r1, r2)]
                       for r1, r2 in zip(self.matrix, other)])

    # @property
    def size(self):
        rows = len(self.matrix)
        cols = 0
        for row in self.matrix:
            if len(row) > cols:
                cols = len(row)

        return rows, cols

# Заполнить с пробелами lngth
# print(f"{variable: >lngth}")


a = [[1,2,3],[4,5,6],[7,8,9]]
m = Matrix(a)
print(m)
m[0][1] = 99
print(m)
print(m.size())
#exec(stdin.read())
