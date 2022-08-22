violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

summTime = 0
numb = int(input('Сколько песен выбрать? '))
for i_numb in range(1, numb + 1):
    print('Название песни', i_numb, end=' ')
    song = input()
    for i_trek in range(len(violator_songs)):
        if song == violator_songs[i_trek][0]:
            songTime = violator_songs[i_trek][1]
            summTime += songTime
print('Общее время звучания песен:', summTime, 'минут')