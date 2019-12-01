boxs = open("input.txt").read().split("\n")[:-1]
ribbon = 0
for i in boxs:
    i = sorted([int(j) for j in i.split("x")])
    ribbon+=(i[0]*2+i[1]*2)+(i[0]*i[1]*i[2])
print(ribbon)
