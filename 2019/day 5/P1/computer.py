codes = open("input.txt").read().split(",")
codes = [int(i) for i in codes]

inp = input(">")

out = str()
i=0
while i < len(codes):
    s = str(codes[i])
    action = int(s[-1])
    par = [int(i) for i in list(s[:-2])][::-1]
    
    if action in [1,2] and len(par) < 2:
        r = 2
    elif action in [3,4] and len(par) < 1:
        r = 0
    for j in range(len(par), r-len(par)):
        par.append(0)


    for j, p in enumerate(par[:-1]):
        par[j] = codes[i+j+2] if p else codes[codes[i+j+2]]
 
    if action == 1:
        codes[codes[i+3]] = par[0] + par[1]
        i+=4
    elif action == 2:
        codes[codes[i+3]] = par[0] * par[1]
        i+=4
    elif action == 3:
        codes[codes[i+1]] = inp
        i+=2
    elif action == 4:
        out += str(codes[codes[i+1]])
        i+=2

    elif action == 9:
        break
    else:
        err = 1
        break
print(codes[0])
