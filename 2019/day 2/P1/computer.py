codes = open("input.txt").read().split(",")
codes = [int(i) for i in codes]

codes[1] = 12
codes[2] = 2

i=0
while i < len(codes) and codes[i] != 99:
    if codes[i] == 1:
        codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
    elif codes[i] == 2:
        codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
    i+=4
print(codes[0])
