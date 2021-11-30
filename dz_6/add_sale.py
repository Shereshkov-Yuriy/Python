from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as f:
    if len(argv) > 1 and [i for i in argv[1:] if i.replace('.', '').replace(',', '').isdigit()]:
        f.write(argv[1].replace(',', '.') + '\n')
    else:
        print('Не является числом.')
