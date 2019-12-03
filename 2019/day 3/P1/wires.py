wiers = open("input.txt").read().split("\n")
wiers[0] = wiers[0].split(",")
wiers[1] = wiers[1].split(",")
del wiers[2]

cords = {}

c = 0
for w in wiers:
    x = 0
    y = 0
    c+=1
    for i in w:
        for j in range(int(i[1:])): 
            if i[0] == "U":
                y+=1
            elif i[0] == "D":
                y-=1
            elif i[0] == "R":
                x+=1
            elif i[0] == "L":
                x-=1
            if f"{x};{y}" not in cords:
                cords[f"{x};{y}"] = [c]
            else:
                cords[f"{x};{y}"].append(c)

manhattan=[]
for i in cords:
    if len(cords[i]) >= 2 and cords[i][0] == 1 and cords[i][1] == 2:
        print(cords[i])
        c = i.split(";")
        x = int(c[0])
        y = int(c[1])
        manhattan.append((abs(x-0))+(abs(y-0)))
print(min(manhattan))
