seats = open("input.txt").read().split("\n")[:-1]
plane = [[i*8+j for j in range(8)] for i in range(128)]
taken = []

for seat in seats:
    p = plane
    for h in seat[:7]:
        if h == "F":
            p = p[:len(p)//2]
        else:
            p = p[len(p)//2:]
    p = p[0]
    for h in seat[7:]:
        if h == "L":
            p = p[:len(p)//2]
        else:
            p = p[len(p)//2:]
    taken.append(p[0])

print(list(filter(lambda x: x not in taken and x+1 in taken and x-1 in taken, range(1024)))[0])
