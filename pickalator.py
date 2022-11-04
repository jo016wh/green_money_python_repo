import random
import time

team1_name = "BYU"
team1_rank = 8
team2_name = "Texas"
team2_rank = 9


team1_chance = 16 - team1_rank
team2_chance = 16 - team2_rank

team1_chance += random.randint(0,16)
team2_chance += random.randint(0,16)

print('The pickalator\n is now choosing a winner...\n')

time.sleep(3)

print('...almost\nthere...\n')

time.sleep(3)

if team1_chance > team2_chance:
    print('team 1 wins!')
else:
    print('team 2 wins!')

    print(f'team 1 chance: {team1_chance}')
    print(f'team 2 chance: {team2_chance}')

