# A
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
for i in prices:
    print(f'{int(i):02d} руб. {int(i * 100 % 100):02d} коп.', end=', ')
print('\n')
# B
print(id(prices))
prices.sort()
print(prices, id(prices))
print('\n')
# C
prices_sort_down = sorted(prices, reverse=True)
print(prices_sort_down, id(prices_sort_down))
print('\n')
# D
print(sorted(prices_sort_down[0:5]))
