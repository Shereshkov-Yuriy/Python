with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    gen = ((line.split()[0], line.replace('"', '').split()[5], line.split()[6]) for line in f)
    for i in gen:
        print(i)
