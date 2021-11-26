with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    spam_dict = {}
    for i in f:
        i = i.split()[0]
        if i in spam_dict:
            spam_dict[i] += 1
        else:
            spam_dict[i] = 1

spam_request = max(spam_dict.values())
for key, val in spam_dict.items():
    if val is spam_request:
        print('IP спамера: ', key, 'Запросов: ', spam_request, sep='\n')
