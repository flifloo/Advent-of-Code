expense_report = [int(i) for i in open("input.txt").read().split("\n")[:-1]]

for i in expense_report:
    j = 2020-i
    if j in expense_report:
        print(i*j)
        break
