strings = open("input.txt").read().split("\n")[:-1]
nice = 0
for i in strings:
    double = False
    for j in range(len(i)-1):
        if i.count(f"{i[j]}{i[j+1]}") >= 2 and f"{i[j]}{i[j]}{i[j]}" not in i:
            double = True
            break
    for j in range(len(i)):
        f2 = i.find(i[j], j+1)
        if f2-j == 2 and double:
            nice+=1
            break
print(nice)

