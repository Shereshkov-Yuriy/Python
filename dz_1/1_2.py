full_sum = 0
# Изучая документацию, нашел интересный способ создания списка в одну строку.
cubes_odd = [x ** 3 for x in range(1, 1000, 2)]
# print(cubes_odd)
for x, number in enumerate(cubes_odd):
    sum_num = 0
    while number:
        sum_num += number % 10
        number = number // 10
    if not sum_num % 7:
        full_sum += cubes_odd[x]
print(full_sum)
# Результат: 17485588610.
# Задача B. Создадим новый список.
full_sum = 0
cubes_odd_new = [cubes_odd[x] + 17 for x in range(len(cubes_odd))]
for x, number in enumerate(cubes_odd_new):
    sum_num = 0
    while number:
        sum_num += number % 10
        number = number // 10
    if not sum_num % 7:
        full_sum += cubes_odd_new[x]
print(full_sum)
# Результат: 15392909930.
# Задача С: Решение задачи В без создания дополнительного списка.
full_sum = 0
cubes_odd = [cubes_odd[x] + 17 for x in range(len(cubes_odd))]
for x, number in enumerate(cubes_odd):
    sum_num = 0
    while number:
        sum_num += number % 10
        number = number // 10
    if not sum_num % 7:
        full_sum += cubes_odd[x]
print(full_sum)
# Результат: 15392909930.
