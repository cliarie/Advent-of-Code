from collections import defaultdict
with open("d4.txt", "r") as file_in:
  lines = [x.strip() for x in file_in.readlines()]

def getpoints(card, string, cards):
    count = 0
    game = string.split(":")
    winning = game[1].split("|")[0].split()
    nums = game[1].split("|")[1].split()
    for n in nums:
        if n in winning:
            count += 1
    # print(card, count)
    # cards[card] = count
    cards[card] += 0
    for i in range(count):
        cards[card + i + 1] += 1 * cards[card]
        # print(i+1)
    # return count


if __name__ == '__main__':
    total = 0
    card = 1
    cards = defaultdict(lambda:1)
    for string in lines:
        getpoints(card, string, cards)
        card += 1
    for k, v in cards.items():
        total += v
    print(total)