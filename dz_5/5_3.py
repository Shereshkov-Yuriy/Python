import itertools

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

gen = ((t, k) for t, k in itertools.zip_longest(tutors, klasses[:len(tutors)], fillvalue='None'))
print(type(gen))

for i in gen:
    print(i, end="\n")

# Проверка, что генератор истощен.
print(list(itertools.islice(gen, 1)))
