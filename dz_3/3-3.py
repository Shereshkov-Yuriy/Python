names = ('Мария', 'Иван', 'Петр', 'Илья')
names_dict = {}


def thesaurus(*args):
    for name in sorted(args):
        if not names_dict.get(name[0:1]):
            names_dict[name[0:1]] = [name]
        else:
            names_dict[name[0:1]].append(name)
    return names_dict


print(thesaurus(*names))
