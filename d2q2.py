with open("input.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

#12 red cubes, 13 green cubes, and 14 blue cubes

def checkgame(string):
    max = {
        "red": 0,
        "green": 0, 
        "blue": 0
    }
    game = string.split(':')
    id = int(game[0].split()[1])
    gameset = game[1].split(';')
    for i in range(len(gameset)):
        draw = gameset[i].split(',')
        for j in range(len(draw)):
            cubes = draw[j].split()
            if int(cubes[0]) > max[cubes[1]]:
                max[cubes[1]] = int(cubes[0])
    print(max["red"], max["blue"], max["green"])
    return(max["red"] * max["blue"] * max["green"])


if __name__ == '__main__':
    sum = 0
    for string in lines:
        sum += checkgame(string)
        print(checkgame(string))
    print(sum)