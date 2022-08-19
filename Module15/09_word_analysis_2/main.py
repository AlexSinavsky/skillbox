word = input('Введите слово: ')
letterBase = list(word)
long = len(word)
count = 0
for i in range(long // 2):
    if letterBase[i] == letterBase[long - 1 - count]:
        count += 1
if count == long // 2:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')



