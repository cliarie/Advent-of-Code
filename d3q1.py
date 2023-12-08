with open("input-3.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

a = [1, 0, -1, 0, 1, 1, -1, -1]
b = [0, 1, 0, -1, 1, -1, 1, -1]

def inbounds(x, y, m, n):
    return (x >= 0 and y >= 0 and x < m and y < n)

def checkengine(matrix):
    sum = 0
    num = ""
    valid = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                num += matrix[i][j]
                for k in range(8):
                    if inbounds(i+a[k], j+b[k], len(matrix), len(matrix[i])) and matrix[i+a[k]][j+b[k]] != '.' and not matrix[i+a[k]][j+b[k]].isdigit():
                        valid = True
            if j == len(matrix[i]) - 1 or not matrix[i][j].isdigit():
                if valid:
                    valid = False
                    sum += int(num)
                    print(num)
                num = ""
    return sum

if __name__ == '__main__':
    m = []
    for string in lines:
        m.append(string)
    print(checkengine(m))