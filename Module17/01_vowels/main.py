vowelBase = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')
vowelInText = [letters for letters in text if letters in vowelBase]

print('Список гласных букв', vowelInText,'\nДлина списка:', len(vowelInText))

            
