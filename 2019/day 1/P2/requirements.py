modules = open("input.txt").read().split("\n")[:-1]
requirement = 0
for i in modules:
    fule=(int(i)//3)-2
    while fule > 0:
        requirement+=fule
        fule=(fule//3)-2
print(requirement)
