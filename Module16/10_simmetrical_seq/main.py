def is_palindrome(base):
    reversBase = []
    for num in range(len(base) -1, -1, -1):
        reversBase.append(base[num])
    if base == reversBase:
        return True
    else:
        return False

numb = int(input('Количество цифр: '))
numbBase = []
for _ in range(numb):
    numbers = int(input('Число: '))
    numbBase.append(numbers)

new_nums = []
answer = []
for i_nums in range(0, len(numbBase)):
    for j_elem in range(i_nums, len(numbBase)):
        new_nums.append(numbBase[j_elem])
    if is_palindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(numbBase[i_answer])
        answer.reverse()
        break
    new_nums = []
print('Исходный список:', numbBase)
print('Нужно чисел для палиндрома:', len(answer))
print('Список этих чисел:', answer)