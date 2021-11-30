from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", 'еще', 'туда']
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []


def get_jokes(n, flag=False):
    """
    Makes a list of jokes from word lists.

    :param n: number of jokes
    :param flag: unique / non-unique
    :return: list of random jokes

    """
    if flag:
        if n > len(min(nouns, adverbs, adjectives)):
            n = len(min(nouns, adverbs, adjectives))
        for i in range(n):
            a, b, c = choice(nouns), choice(adverbs), choice(adjectives)
            nouns.remove(a)
            adverbs.remove(b)
            adjectives.remove(c)
            jokes.append(''.join(f'{a} {b} {c}'))
        return jokes
    else:
        for i in range(n):
            jokes.append(''.join(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'))
        return jokes


print(get_jokes(100, True))
