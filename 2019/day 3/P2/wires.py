wiers = open("input.txt").read().split("\n")
wiers[0] = wiers[0].split(",")
wiers[1] = wiers[1].split(",")
del wiers[2]

cords = [["O;O"], ["0;0"]]

c = 0
for w in wiers:
    x = 0
    y = 0
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
                cords[c].append(f"{x};{y}")
    c+=1

times=[]
for i in cords[0]:
    if i in cords[1]:
        w1 = cords[0].index(i)
        w2 = cords[1].index(i)
        times.append(w1+w2)

print(min(times))
