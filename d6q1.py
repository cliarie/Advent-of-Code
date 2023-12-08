import cmath
import math
with open("d6.txt") as file_in:
    _, time = file_in.readline().split(": ")
    _, distance = file_in.readline().split(": ")

# time in [1, distance)
# > record distance -> min and max for how long to hold
# try record distance + 1 = (time - x) * (x)
# solve -x^2 + t(x) - (d+1)= 0

def button(t, d):
    discrim = ((t)**2) - (-4*(-d-1))
    sol1 = (-(t)-cmath.sqrt(discrim))/(-2)
    sol2 = (-(t)+cmath.sqrt(discrim))/(-2)
    sol1 = math.floor(sol1.real)
    sol2 = math.ceil(sol2.real)
    return sol1 - sol2 + 1

if __name__ == '__main__':
    time = time.split()
    distance = distance.split()
    prod = 1
    for i in range(len(time)):
        prod *= button(int(time[i]), int(distance[i]))
    print(prod)