from collections import Counter
import functools
with open("d7.txt") as file_in:
    lines = file_in.readlines()

strength = "AKQT98765432J"

def compare(item1, item2):
    item1, _ = item1
    item2, _ = item2
    for i in range(len(item1)):
        if strength.index(item1[i]) == strength.index(item2[i]):
            continue
        if strength.index(item1[i]) < strength.index(item2[i]):
            return -1
        return 1

def j(cards, x, js):
    if not cards:
        return js
    if cards[x][0] != 'J':
        if (x == 1 and cards[0][0] != 'J'):
            return cards[x][1]

        return max(cards[x][1] + js, js)
    return js

def order(m):
    m = dict(sorted(m.items(), key=functools.cmp_to_key(compare)))
    order = {k: v for v, k in enumerate(strength)}
    order1 = {}
    for k, v in m.items():
        js = Counter(k)['J']
        string = k.replace('J', '')
        cards = Counter(string).most_common(2)
        if j(cards, 0, js) == 5:
            order1[(v, k)] = 1 
        elif j(cards, 0, js) == 4:
            order1[(v, k)] = 2 
        elif j(cards, 0, js) == 3:
            if j(cards, 1, js) == 2:
                order1[(v, k)] = 3 
            else:
                order1[(v, k)] = 4 
        elif j(cards, 0, js) == 2:
            if j(cards, 1, js) == 2:
                order1[(v, k)] = 5 
            else:
                order1[(v, k)] = 6 
        else:
            order1[(v, k)] = 7 + js
    return dict(dict(sorted(order1.items(), key=lambda x:x[1])).keys())

if __name__ == '__main__':
    decktobid = dict()
    for l in lines:
        decktobid[(l.split()[0])] = int(l.split()[1])
    decktobid = order(decktobid)
    winnings, rank = 0, len(decktobid)

    for bid in decktobid.keys():
        winnings += bid * rank
        rank -= 1
    print(winnings)
