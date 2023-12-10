import re
import math
import itertools

with open("d9.txt") as file_in:
    lines = file_in.readlines()

def extrapolate(seq):
    if all(v==0 for v in seq):
        return 0
    differences = [seq[i+1]-seq[i] for i in range(len(seq) - 1)]
    return (seq[-1] + extrapolate(differences))


if __name__ == '__main__':
    history = []
    for line in lines:
        seq = [int(x) for x in line.split()]
        history.append(extrapolate(seq))
    print(sum(history))