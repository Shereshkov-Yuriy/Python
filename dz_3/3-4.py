names_list = ('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')
names_dict = {}


def thesaurus_adv(*args):
    for full_name in sorted(args):
        name, surname = full_name.split()
        s_val = names_dict.setdefault(surname[0], {name[0]: [full_name]})
        n_val = s_val.setdefault(name[0], [full_name])
        if full_name not in n_val:
            n_val.append(full_name)
    return names_dict


print(thesaurus_adv(*names_list))
