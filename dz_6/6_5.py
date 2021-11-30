from sys import argv
from itertools import zip_longest

in_users, in_hobby, out_file = argv[1:]

with open(in_users, 'r', encoding='utf-8') as users:
    with open(in_hobby, 'r', encoding='utf-8') as hobby:
        user_hobby = zip_longest((' '.join(user.split(',')) for user in users), hobby, fillvalue=None)

        with open(out_file, 'w', encoding='utf-8') as f:
            for i in user_hobby:
                print(f'{str(i[0]).strip()}: {str(i[1]).strip()}', file=f)
