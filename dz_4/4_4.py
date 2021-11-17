import my_module as my

val_cur, date_cur = my.currency_rates('uSd')
print(f'{val_cur}, {date_cur}')
val_cur, date_cur = my.currency_rates('euR')
print(f'{val_cur}, {date_cur}')
val_cur, date_cur = my.currency_rates('dfhjdghj')
print(f'{val_cur}, {date_cur}')
