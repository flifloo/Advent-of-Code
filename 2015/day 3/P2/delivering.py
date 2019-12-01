instructions = open("input.txt").read()
cords={"Santa": [0,0], "Robot Santa": [0,0]}
house = ["0;0"]
delivery = 0
turn = "Santa"
for i in list(instructions):
    if i == "^":
        cords[turn][1]+=1
    elif i == "v":
        cords[turn][1]-=1
    elif i == ">":
        cords[turn][0]+=1
    elif i == "<":
        cords[turn][0]-=1
    if f"{cords[turn][0]};{cords[turn][1]}" not in house:
        house.append(f"{cords[turn][0]};{cords[turn][1]}")
    turn = "Santa" if turn == "Robot Santa" else "Robot Santa"
print(len(house))
