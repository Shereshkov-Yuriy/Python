def gen(max):
    for num in range(1, max + 1, 2):
        yield num


for x in gen(15):
    print(x)

# Или так.
print(*gen(15), sep=', ')
