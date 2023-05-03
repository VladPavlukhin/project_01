# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

min_value = 0
max_value = 0


def minimum(arr_v):
    global min_value
    min_value = arr_v[0]
    for s in arr_v:
        if s < min_value:
            min_value = s
    return min_value


def maximum(arr_v):
    global max_value
    max_value = arr_v[0]
    for s in arr_v:
        if s > max_value:
            max_value = s
    return max_value


# arr_val = [4, 6, 2, 1, 9, 63, -134, 566]
# arr_val = [-52, 56, 30, 29, -54, 0, -110]
arr_val = [42, 54, 65, 87, 0]
# arr_val = [5]
print(f'max = {minimum(arr_val)}, min = {maximum(arr_val)}')

