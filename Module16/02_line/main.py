firstClas = list(range(160, 177, 2))
secondClas = list(range(160, 181, 3))
print('Ученики первого класса по росту', firstClas)
print('Ученики второго класса по росту', secondClas)

firstClas.extend(secondClas)
for i_kids in range(len(firstClas)):
    for kids in range(i_kids + 1, len(firstClas)):
        if firstClas[i_kids] > firstClas[kids]:
            firstClas[i_kids], firstClas[kids] = firstClas[kids], firstClas[i_kids]
print('Объединенный список учеников по росту', firstClas)
