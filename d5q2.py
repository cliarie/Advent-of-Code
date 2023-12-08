with open("d5.txt", "r") as file_in:
  file = file_in.read().split("\n\n")
  seeds = file[0][7:].split()
  maps = [file[i].split("\n")[1:] for i in range(1, len(file))]

# maps ss, sf, fw, wl, lt, th, hl same functions

# rng[0]        where sht happens               rng[1]
# rng[0]    start           start+dist          rng[1]

def getrange(m, s):
    changed = []
    for ranges in m:
        end, start, dist = ranges.split()
        unchanged = [] # can only be changed once in a map
        while s:
            rng = s.pop()
            if int(start) >= rng[1] or (int(start) + int(dist)) <= rng[0]:
                unchanged.append(rng)
                continue
            pre = (rng[0], max(rng[0], int(start)))
            mid = (max(int(start), rng[0]), min(rng[1], int(start) + int(dist)))
            post = (min(int(start) + int(dist), rng[1]), rng[1])
            if pre[0] < pre[1]:
                unchanged.append(pre)
            if mid[0] < mid[1]:
                changed.append((mid[0] + int(end) - int(start), mid[1] + (int(end) - int(start))))
            if post[0] < post[1]:
                unchanged.append(post)
        s = unchanged
    return changed + s

if __name__ == '__main__':
    seeds = [int(x) for x in seeds]
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    locs = []
    for s in seeds:
        r = [s]
        for m in maps:
            r = getrange(m, r)
        locs += r
    print(min(locs)[0])