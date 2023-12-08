from collections import defaultdict
with open("d4.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

def getpoints(string):
    points = 0
    game = string.split(":")
    winning = game[1].split("|")[0].split()
    nums = game[1].split("|")[1].split()
    print(winning)
    for n in nums:
        if n in winning:
            if points == 0:
                points = 1
            else:
                points = points * 2
    print(points)
    return points


if __name__ == '__main__':
    total = 0
    for string in lines:
        total += getpoints(string)
    print(total)