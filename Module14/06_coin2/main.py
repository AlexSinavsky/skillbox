import math
print('Введите координаты')
x = float(input('Х: '))
y = float(input('Y: '))
rad = float(input('Введите радиус: '))
print()
gip = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
if gip <= rad:
  print('Монетка где то рядом')
else:
  print('Монетки в области нет')
