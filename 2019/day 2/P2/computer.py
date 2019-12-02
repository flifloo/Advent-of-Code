codes = open("input.txt").read().split(",")
noun = -1
verb = -1
while noun <= 99:
    noun+=1
    verb=-1
    while verb <= 99:
        verb+=1
        codes = open("input.txt").read().split(",")
        codes = [int(i) for i in codes]

        codes[1] = noun
        codes[2] = verb

        i=0
        while codes[i+3] < len(codes) and codes[i] != 99:
            if codes[i] == 1:
                codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
            elif codes[i] == 2:
                codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
            i+=4
        if codes[0] == 19690720:
            print(f"{100*noun+verb}")
            exit()
