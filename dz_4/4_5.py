import sys
from my_module import currency_rates

# Вариант 1.
_, args = sys.argv
val_cur, date_cur = currency_rates(args)
print(f'{val_cur}, {date_cur}')


# Вариант 2.
# val_cur, date_cur = currency_rates(*sys.argv[1:])
# print(f'{val_cur}, {date_cur}')
