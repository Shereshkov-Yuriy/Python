from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        users_list = [line.strip() for line in users]
        hobby_list = [line.strip() for line in hobby]

if len(users_list) > len(hobby_list):
    user_book = dict(zip_longest((' '.join(user.split(',')) for user in users_list), hobby_list, fillvalue=None))
    with open('users_hobby.json', 'w', encoding='utf-8') as f:
        json.dump(user_book, f, ensure_ascii=False, indent=4)
else:
    exit(1)

with open('users_hobby.json', 'r', encoding='utf-8') as f:
    print(json.load(f))
