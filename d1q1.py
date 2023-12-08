with open("input.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

def calibrate(string):
    firstdig, secdig = -1, -1
    for c in string:
        if c.isdigit():
            firstdig = int(c)
            break
    for i in range(len(string)):
        if string[len(string) - 1 - i].isdigit():
            secdig = int(string[len(string) - 1 - i])
            break
    return firstdig * 10 + secdig

if __name__ == '__main__':
    sum = 0
    for string in lines:
        sum += calibrate(string)
    print(sum)