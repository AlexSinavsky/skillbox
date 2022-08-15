def revers(x):
  revX = 0
  x //= 1
  while x > 0:
    revX = revX * 10 + x % 10
    x //= 10
  return revX

def decimal (text):
    text = str(text)
    dec = ''
    turn = 0
    count = 0
    for letters in text:
        if turn == 1:
            dec += letters
            count += 1
        elif letters == '.':
            turn = 1
    revDec = revers(int(dec)) / 10 ** count
    return revDec

n = float(input('Введите число N: '))
k = float(input('Введите число K: '))
print()
revN1 = revers(n)
revN2 = decimal(n)
print('Первое число наоборот:', revN1 + revN2)

revK1 = revers(k)
revK2 = decimal(k)
print('Второе число наоборот:', revK1 + revK2)
print('Сумма:', revN1 + revN2 + revK1 + revK2)
print()


