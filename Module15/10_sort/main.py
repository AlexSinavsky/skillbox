base = [1, 4, -3, 0, 10]
baseNew = []
long = len(base)
longNew = len(baseNew)
minNum = base[0]
for numb in base:
    if numb < minNum:
        minNum = numb
baseNew.append(minNum)

print(baseNew)
