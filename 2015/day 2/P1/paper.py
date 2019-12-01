boxs = open("input.txt").read().split("\n")[:-1]
paper = 0
for i in list(boxs):
    i = i.split("x")
    dim1 = (int(i[0])*int(i[1]))
    dim2 = (int(i[1])*int(i[2]))
    dim3 = (int(i[2])*int(i[0]))
    paper+=2*dim1+2*dim2+2*dim3+min([dim1, dim2, dim3])
print(paper)
