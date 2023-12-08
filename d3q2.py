from collections import defaultdict
with open("d3.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

a = [1, 0, -1, 0, 1, 1, -1, -1]
b = [0, 1, 0, -1, 1, -1, 1, -1]

def inbounds(x, y, m, n):
    return (x >= 0 and y >= 0 and x < m and y < n)

def getratios(matrix):
    sum = 0
    num = ""
    valid = False
    gears = set()
    geardict = defaultdict(list)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                num += matrix[i][j]
                for k in range(8):
                    if inbounds(i+a[k], j+b[k], len(matrix), len(matrix[i])) and matrix[i+a[k]][j+b[k]] == "*":
                        gears.add((i+a[k], j+b[k]))
                        valid = True
            if j == len(matrix[i]) - 1 or not matrix[i][j].isdigit():
                if valid:
                    valid = False
                    for g in gears:
                        geardict[g].append(int(num))
                    gears = set()
                num = ""
    
    for k, v in geardict.items():
        print(k)
        print(v)

    for l in geardict.values():
        if len(l) == 2:
            sum += l[0] * l[1]
    return sum

if __name__ == '__main__':
    m = []
    for string in lines:
        m.append(string)
    print(getratios(m))