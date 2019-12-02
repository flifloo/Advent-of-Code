strings = open("input.txt").read().split("\n")[:-1]
nice = 0
for i in strings:
    pair = False
    double = False
    for j in range(len(i)-1):
        if not pair:
            if i.count(f"{i[j]}{i[j+1]}") >= 2 and f"{i[j]}{i[j]}{i[j]}" not in i:
                pair = True
        if not double:
            f2 = i.find(i[j], j+1)
            if f2-j == 2:
                double = True
        if pair and double:
            nice+=1
            break
print(nice)

