pswrange = [int(i) for i in open("input.txt").read().split("-")]

valid = 0
for i in range(pswrange[0], pswrange[1]):
    i = str(i)
    l = list(i)
    c = 0
    dec = False
    double = False
    while c < len(l)-1:
        if l[c] <= l[c+1]:
            pass
        else:
            dec = True
            break
        if f"{l[c]}{l[c]}" in i and not f"{l[c]}{l[c]}{l[c]}" in i:
            double = True
        c+=1
    if not dec and double:
        valid+=1

print(valid)

