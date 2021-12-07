src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# Вариант 1. Решение в "лоб".
src_result = [i for i in src if src.count(i) == 1]
print(src_result)

# Вариант 2. Оптимизация.
src_dict = {i: 0 for i in src}

for i in src:
    src_dict[i] += 1

src_result_2 = [i for i in src_dict.keys() if src_dict[i] == 1]
print(src_result_2)
