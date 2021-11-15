text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
text_new = []

for idx, val in enumerate(text):
    text_new.append(val)
    if val[:1] == '+' or val[:1] == '-':
        symbol = val[:1]
        _, val = val.split(val[:1])
        text_new[idx] = f'"{symbol}{int(val):02d}"'
    elif val.isdigit():
        text_new[idx] = f'"{int(val):02d}"'

result = ' '.join(text_new)
print(result)
