from functools import reduce


m = [m for m in open("input.txt").read().split("\n")[:-1]]


tl = []
for i in ((1,1), (1, 3), (1, 5), (1, 7), (2,1)):
    j = (0, 0) # y, x
    t = 0
    while j[0] < len(m):
        if m[j[0]][(j[1] % len(m[0]))] == "#":
            t += 1
        j = (j[0] + i[0], j[1] + i[1])
    tl.append(t)

print(reduce(lambda y, x: y*x, tl))
