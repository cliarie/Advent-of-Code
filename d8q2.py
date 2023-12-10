import re
import math
import itertools

with open("d8.txt") as file_in:
    instructions, lines = file_in.read().split('\n\n')

def step(ins, dic, first):
    cur = first
    iter = itertools.cycle(ins)
    count = 1
    for i in iter:
        if dic[cur][int(i)].endswith('Z'):
            return count
        cur = dic[cur][int(i)]
        count+=1
    return 0

if __name__ == '__main__':
    instructions = instructions.replace('R', '1').replace('L', '0')
    dic = re.split('\n| = |, ', lines.replace('(','').replace(')',''))
    dic = {dic[i*3]:[dic[i*3+1], dic[i*3 + 2]] for i in range(len(dic)//3)}

    ans = []
    for start in dic.keys():
        if start.endswith("A"):
            ans.append(step(instructions, dic, start))
    print(math.lcm(*ans))
