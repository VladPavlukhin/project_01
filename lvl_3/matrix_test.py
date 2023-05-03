class Matrix:
    """A simple wrapper around a two-dimensional list"""
    """Простая обёртка вокруг 2-мерного списка - пример"""

    def __init__(self, lst=[[]]):
        self._lst = lst

    # ...
    def __getitem__(self, index):
        return self._lst[index]

    def __setitem__(self, index, val):
        self._lst[index] = val

    def __delitem__(self, index):
        del self._lst[index]

    def __iter__(self):
        return self._lst.__iter__()

    def __len__(self):
        return len(self._lst)

    def __contains__(self, item):
        return item in self._lst

    def __add__(self, other):
        assert type(other) is Matrix
        return Matrix([[e1 + e2 for e1, e2 in zip(r1, r2)]
                       for r1, r2 in zip(self._lst, other)])


class Matrix(Matrix):
    def __str__(self):
        from functools import partial
        def _frmt(el, max_len=0):
            # r = f"{el:>{max_len}}"  # PEP 498 -- Literal String Interpolation
            # с Python 3.6
            r = "{:>{}}".format(el, max_len)  # Медленнее, сложнее

            return r

        srepr = ""
        max_len = 0
        max_len = max((len(str(elem))
                       for row in self._lst
                       for elem in row),
                      default=0)
        _frmt = partial(_frmt, max_len=max_len)

        for row in self._lst:
            srepr += " ".join(map(_frmt, map(str, row))) + "\n"

        return srepr


# Протестируем
m1 = Matrix([[11, 12, 13, 14], [21, 22, 23, 24],
             [31, 32, 33, 34], [41, 42, 43, 44]])

m2 = Matrix([[1, 1, 1, 1], [2, 2, 2, 2],
             [3, 3, 3, 3], [4, 4, 4, 4]])

print(m1)
#print(m2)
print(m1[0][1])
#print(m1 + m2)

m1[0][1] = 99

print(m1)
