import numpy as np

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = np.mean(players)

std = np.std(players)

upper = mean + std

lower = mean - std

count = 0

for i in players:
    if i >= upper:
        count += 1
    elif i <= lower:
        count += 1


print(mean)

print(std)

print(10 - count)
