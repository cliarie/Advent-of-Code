with open("input.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]
  n, points = lines[0], lines[1:]

# max len of spelled out words is 5; min len is 3
lettermap = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

def calibrate(string):
    firstdig, secdig = -1, -1
    for i in range(len(string)):
        if string[i].isdigit():
            if firstdig != -1:
                secdig = int(string[i])
            else:
                firstdig = int(string[i])
            continue
        for j in range(3):
            # print(string[i:i+3+j])
            if string[i:i+3+j] in lettermap:
                if firstdig != -1:
                    secdig = lettermap[string[i:i+3+j]]
                else:
                    firstdig = lettermap[string[i:i+3+j]]
                break
    if secdig == -1:
        secdig = firstdig
    return firstdig * 10 + secdig

if __name__ == '__main__':
    sum = 0
    for string in lines:
        sum += calibrate(string)
    print(sum)