from collections import deque

#hard coded directions S goes from reading personal input

with open("d10.txt") as file_in:
    lines = file_in.readlines()

symbol = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": [(-1, 0),(0, -1)]
}

def inbounds(grid, a):
    return a[0] >=0 and a[1] >=0 and a[0] < len(grid) and a[1] < len(grid[0])

def traverse(grid, b):
    visited = set()
    q = [(b, 0)]
    maxc = 0
    while q:
        a, count = q.pop(0)
        if grid[a[0]][a[1]] == '.' or a in visited or not inbounds(grid, a):
            continue
        maxc = max(maxc, count)
        visited.add(a)
        sym = grid[a[0]][a[1]]
        grid[a[0]][a[1]] = count
        if sym in symbol:
            for x in symbol[sym]:
                q.append((tuple(map(lambda i, j: i + j, a, x)), count + 1))
    for x in grid:
        print(x)
    return maxc

if __name__ == '__main__':
    grid = []
    pos = (0, 0)
    for line in lines:
        grid.append([x for x in line.strip()])
    for i, x in enumerate(grid):
        if 'S' in x:
            a = (i, x.index('S'))
    m = traverse(grid, a)
    print(m)
