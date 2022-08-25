import random

stickNum = int(input('Количество палок: '))
castNum = int(input('Количество бросокв: '))
stickBase = ['I' for _ in range(stickNum)]

for i_cast in range(1, castNum + 1):
    left = random.randint(1, 10)
    right = random.randint(1, 10)
    left = min(left, right)
    right = max(left, right)
    print('Бросок', i_cast, 'сбиты палки с номера', left, 'по номер', right)
    for i_stick in range(left, right + 1):
        stickBase[i_stick] = '.'
print('Результат:',''.join(stickBase))