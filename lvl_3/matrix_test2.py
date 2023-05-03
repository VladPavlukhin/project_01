from functools import lru_cache
from itertools import product
from typing import (Any,
                    Iterable,
                    Iterator)


class Matrix:
    def __init__(self,
                 height: int,
                 width: int,
                 fill_value: Any = 0) -> None:
        self.height = height
        self.width = width
        self.rows = [[fill_value] * width for _ in range(height)]

    def __str__(self) -> str:
        return "\n".join(map(str, self.rows))

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.height!r}, {self.width!r})'

    @lru_cache(1)
    def __len__(self) -> int:
        return self.height * self.width

    def __add__(self, matrix2):
        raise NotImplementedError

    def __mul__(self, matrix2):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError


#m1 = Matrix([[11, 12, 13, 14], [21, 22, 23, 24],
#             [31, 32, 33, 34], [41, 42, 43, 44]])

#m2 = Matrix([[1, 1, 1, 1], [2, 2, 2, 2],
#             [3, 3, 3, 3], [4, 4, 4, 4]])

f = 5
m1 = Matrix(5, 4, f)
m2 = Matrix(3, 3)

print(m1)
print(m2)
