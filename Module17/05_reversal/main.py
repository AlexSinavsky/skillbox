text = 'dfbhvsdxdhcz'
print('Исходная строка:', text)
print('Измененная строка:', text[:text.find('h')] + text[text.rfind('h'):text.find('h'):-1] + text[text.rfind('h'):])
