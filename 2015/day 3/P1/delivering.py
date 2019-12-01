instructions = open("input.txt").read()
x = 0
y = 0
house = ["0;0"]
delivery = 0
for i in list(instructions):
    if i == "^":
        y+=1
    elif i == "v":
        y-=1
    elif i == ">":
        x+=1
    elif i == "<":
        x-=1
    if f"{x};{y}" not in house:
        house.append(f"{x};{y}")
print(len(house))
