import numpy as np 

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

std = np.std(data)

mean = np.mean(data)

upper = mean + std

lower = mean - std

count = 0

for i in data:
    if i >= upper:
        count += 1
    elif i <= lower:
        count += 1
    else:
        count += 0
        
p = (1 - count / 16) * 100

print(p)