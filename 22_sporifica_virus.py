###################################
# --- Day 22: Sporifica Virus --- #
###################################

import AOCUtils

###################################

grid = AOCUtils.loadInput(22)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # U, R, D, L

h, w = len(grid), len(grid[0])

infected = set()
for x in range(h):
    for y in range(w):
        if grid[x][y] == "#":
            infected.add((x-h//2, y-w//2))

cur = (0, 0)
facing = 0

infectedBursts = 0
for i in range(10000):
    if cur in infected:
        facing += 1 # Right
        infected.remove(cur)
    else:
        facing -= 1 # Left
        infected.add(cur)
        infectedBursts += 1

    dx, dy = directions[facing%4]
    cur = (cur[0]+dx, cur[1]+dy)

print("Part 1: {}".format(infectedBursts))

infected = dict()
for x in range(h):
    for y in range(w):
        if grid[x][y] == "#":
            infected[(x-h//2, y-w//2)] = "#"

cur = (0, 0)
facing = 0

infectedBursts = 0
for i in range(10000000):
    if cur not in infected:
        facing -= 1 # Left
        infected[cur] = "W"
    elif infected[cur] == "W":
        infected[cur] = "#"
        infectedBursts += 1
    elif infected[cur] == "#":
        facing += 1 # Right
        infected[cur] = "F"
    elif infected[cur] == "F":
        facing += 2 # Reverse
        infected.pop(cur)

    dx, dy = directions[facing%4]
    cur = (cur[0]+dx, cur[1]+dy)

print("Part 2: {}".format(infectedBursts))

AOCUtils.printTimeTaken()