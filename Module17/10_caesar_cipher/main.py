text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

textList = list(text)
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = list(alphabet)

textCode = []
new_letter = 0
for letter in textList:
    if letter != ' ':
        new_letter = alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
        textCode.append(new_letter)
    else:
        textCode.append(' ')

print('Зашифрованное сообщение:', ''.join(textCode))