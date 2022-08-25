base = [1, 0, 5, 6, 1, 0, 9, 4]
print('Исходный список', base)
for i_nums in range(len(base)):
    if base[i_nums] == 0:
        base.append(base[i_nums])
        base.remove(base[i_nums])
print('Список с нулями в конце', base)
base = [(x if x != 0 else base.pop(x)) for x in base]
print('Список без нулей', base)

