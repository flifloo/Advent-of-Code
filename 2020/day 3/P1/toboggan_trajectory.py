m = [m for m in open("input.txt").read().split("\n")[:-1]]



i = (0,0)
t = 0
while i[0] < len(m):
    if m[i[0]][(i[1]%len(m[0]))] == "#":
        t += 1
    i = (i[0]+1, i[1]+3)

print(t)
