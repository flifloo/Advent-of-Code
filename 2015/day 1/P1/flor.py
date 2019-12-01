instructions = open("input.txt").read()
flor = 0
for i in list(instructions):
    if i == "(":
        flor+=1
    elif i == ")":
        flor-=1
print(flor)

