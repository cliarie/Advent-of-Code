import re
import itertools

with open("d8.txt") as file_in:
    instructions, lines = file_in.read().split('\n\n')

def step(ins, dic):
    cur = 'AAA'
    iter = itertools.cycle(ins)
    count = 1
    for i in iter:
        print(i)
        print(dic[cur][int(i)])
        if dic[cur][int(i)] == "ZZZ":
            return count
        cur = dic[cur][int(i)]
        count+=1
    return 0

if __name__ == '__main__':
    instructions = instructions.replace('R', '1').replace('L', '0')
    dic = re.split('\n| = |, ', lines.replace('(','').replace(')',''))
    print(len(dic))
    dic = {dic[i*3]:[dic[i*3+1], dic[i*3 + 2]] for i in range(len(dic)//3)}

    print(dic)
    print(step(instructions, dic))