with open("input-2.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

#12 red cubes, 13 green cubes, and 14 blue cubes

limit = {
    "red": 12,
    "green": 13, 
    "blue": 14
}

def checkgame(string):
    game = string.split(':')
    id = int(game[0].split()[1])
    gameset = game[1].split(';')
    for i in range(len(gameset)):
        draw = gameset[i].split(',')
        for j in range(len(draw)):
            cubes = draw[j].split()
            if int(cubes[0]) > limit[cubes[1]]:
                return 0
    return(id)


if __name__ == '__main__':
    sum = 0
    print(checkgame("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))
    for string in lines:
        sum += checkgame(string)
    print(sum)