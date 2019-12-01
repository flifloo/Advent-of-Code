strings = open("input.txt").read().split("\n")[:-1]
nice = 0
for i in strings:
    if i.count("a")+i.count("e")+i.count("i")+i.count("o")+i.count("u") >= 3 \
            and not ("ab" in i or "cd" in i or "pq" in i or "xy" in i):
                for j in list(i):
                    if f"{j}{j}" in i:
                        nice+=1
                        break
print(nice)

