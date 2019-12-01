modules = open("input.txt").read().split("\n")[:-1]
requirement = 0
for i in modules:
    requirement+=(int(i)//3)-2
print(requirement)
