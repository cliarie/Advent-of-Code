with open("d5.txt", "r") as file_in:
  file = file_in.read().split("\n\n")
  seeds = file[0][7:].split()
  maps = [file[i].split("\n")[1:] for i in range(1, len(file))]

# maps ss, sf, fw, wl, lt, th, hl same functions

def getlocation(m):
    done = [False] * len(seeds)
    for ranges in m:
        print(ranges.split())
        end, start, dist = ranges.split()
        for j in range(len(seeds)):
            if seeds[j] >= int(start) and seeds[j] < int(start) + int(dist) and not done[j]:
                seeds[j] += int(end) - int(start)
                done[j] = True

if __name__ == '__main__':
    seeds = [int(x) for x in seeds]
    for m in maps:
        getlocation(m)
    print(seeds)
    print(min(seeds))