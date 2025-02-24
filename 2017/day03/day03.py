import math
input = 265149
# corner val = 265225
corner_val = input
print("----------PART 1----------")
while math.sqrt(corner_val) % 2 != 1:
    corner_val += 1
odd_val = round(math.sqrt(corner_val))
height = width = odd_val
middle = height // 2
# print(corner_val)
# print(odd_val)

# get coords
offset = 0
for i in range(4):
    if input < (corner_val - (i*odd_val) + i) and input > (corner_val+1+i - ((i+1)*odd_val)):
        # calculate offset from the corner
        offset = input - (corner_val+1+i - ((i+1)*odd_val))
        break
# it is on one of the edges, then calc the offset distance from the middle
print(middle + abs(offset-middle))



print("----------PART 2----------")
from itertools import product
i = j = middle
grid = [[0 for _ in range(height)] for _ in range(width)]
val = 1
grid[i][j] = 1
j += 1
count = 0
while val < input:
    count += 1
    print(val, i, j)
    if count % 10 == 0:
        print(val)
    grid[i][j] = val
    if grid[i-1][j] != 0 and grid[i][j+1] == 0:
        # Move right
        j += 1
    elif grid[i][j-1] != 0 and grid[i-1][j] == 0:
        # Move up
        i -= 1
    elif grid[i+1][j] != 0 and grid[i][j-1] == 0:
        # Move left
        j -= 1
    elif grid[i][j+1] != 0 and grid[i+1][j] == 0:
        # Move down
        i += 1
    adds = product((-1, 0, 1), repeat=2)
    val = sum(grid[i+a][j+b] for a, b in adds)

print(val)
