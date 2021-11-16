num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(num_en):
    if num_en.istitle():
        return str(num_dict.get(num_en.lower())).title()
    return num_dict.get(num_en)


# Чтобы проверить несколько раз, упаковал в цикл.
for i in range(4):
    print(num_translate_adv(input('Введи число от 0 до 10 на английском языке: ')))
