import random
team_1 = [random.uniform(5, 10) for _ in range(20)]
team_1 = [round(i_team,2) for i_team in team_1]
team_2 = [random.uniform(5, 10) for _ in range(20)]
team_2 = [round(i_team,2) for i_team in team_2]
team_3 = [(team_1[i] if team_1[i] > team_2[i] else team_2[i]) for i in range(20)]

print('Первая команда', team_1)
print('\nВторая команда', team_2)
print('\nПобедители турнира', team_3)