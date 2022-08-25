text = 'dfbhvsdxdhcz'
print('Исходная строка:', text)
firstH = text.index('h')
revTxt = text[-1::-1]
lastH = len(text) - 1 - revTxt.index('h')
print('Измененная строка:', text[:firstH] + text[lastH:firstH:-1] + text[lastH:])