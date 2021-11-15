text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx, val in enumerate(text):
    if val[:1] == '+' or val[:1] == '-':
        symbol = val[:1]
        _, val = val.split(val[:1])
        text[idx] = f'"{symbol}{int(val):02d}"'
    elif val.isdigit():
        text[idx] = f'"{int(val):02d}"'

result = ' '.join(text)
print(result)
