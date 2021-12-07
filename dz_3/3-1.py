num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num_en):
    num_ru = num_dict.get(num_en)
    return num_ru


# Чтобы проверить несколько раз, упаковал в цикл.
for i in range(4):
    print(num_translate(input('Введи число от 0 до 10 на английском языке: ')))
