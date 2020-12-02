import re


password_re = re.compile(r"^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")


passwords = [password_re.search(p).groups() for p in open("input.txt").read().split("\n")[:-1]]

n = 0
for p in passwords:
    if (p[3][int(p[0])-1] == p[2]) != (p[3][int(p[1])-1] == p[2]):
        n += 1

print(n)
