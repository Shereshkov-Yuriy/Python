for i in range(1, 101):
    if not (i - 11) % 100 or not (i - 12) % 100 or not (i - 13) % 100 or not (i - 14) % 100:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')
