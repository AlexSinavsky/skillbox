base = [1, 4, -3, 0, 10]
print('Неотсортированный список', base)
long = int(len(base))
for i in range(len(base)):
    for numb in range(i + 1, len(base)):
        if base[i] > base[numb]:
            base[i], base[numb] = base[numb], base[i]

print('Отсортированный список', base)
