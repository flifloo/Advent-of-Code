instructions = open("input.txt").read()
flor = 0
for c, i in enumerate(list(instructions)):
    if i == "(":
        flor+=1
    elif i == ")":
        flor-=1
    if flor == -1:
        break
print(c+1)
