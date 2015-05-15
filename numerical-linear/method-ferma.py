from math import pow
eps = 100
POW = 3
MIN = int(10e3)
MAX = int(10e6)
print("From ", MIN, " to ", MAX, ". Eps = ", eps)
for x in list(range(MIN, MAX)):
    for y in list(range(MIN, MAX)):
        for z in list(range(MIN, MAX)):
            if (x != 0 and y != 0 and z != 0 and x < y):
                if ( abs(pow(x, POW) + pow(y, POW) - pow(z, POW)) < eps ):
                    print("\tAnswer with eps", x, y, z)
    print("Iteration: x = ", x)

print("END!")
