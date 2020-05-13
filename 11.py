import math

data = open('number-grid.txt').read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split()
    for j in range(len(data[i])):
       data[i][j] = int(data[i][j])

temp = 0

# check horizontals
for i in range(len(data)):
    for j in range(len(data[i])-3):
        line = data[i]
        prod = line[j] * line[j+1] * line[j+2] * line[j+3]
        if prod > temp: temp = prod

#check verticals
for i in range(len(data)-3):
    for j in range(len(data[i])):
        prod = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j]
        if prod > temp: temp = prod

#check neg-diagonals
for i in range(len(data)-3):
    for j in range(len(data[i])-3):
        prod = data[i][j] * data[i+2][j+2] * data[i+2][j+2] * data[i+3][j+3]
        if prod > temp: temp = prod

#check pos diagonals
for i in range(len(data)-3):
    for j in range(3, len(data[i])):
        prod = data[i][j] * data[i+1][j-1] * data[i+2][j-2] * data[i+3][j-3]
        if prod > temp: temp = prod

print(temp)
