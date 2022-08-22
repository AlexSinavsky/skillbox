shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Введите название детали: ')
count = 0
summPrice = 0
for i_detail in range(len(shop)):
        if shop[i_detail][0] == detail:
                summPrice += shop[i_detail][1]
                count += 1
print('Количество деталей "', detail, '" =', count)
print('Общая стоимость', summPrice)