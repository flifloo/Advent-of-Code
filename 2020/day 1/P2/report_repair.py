expense_report = [int(i) for i in open("input.txt").read().split("\n")[:-1]]

for i in expense_report:
    for j in filter(lambda x: x!= i, expense_report):
        for k in filter(lambda x: x not in [i, j], expense_report):
            if i + j + k == 2020:
                print(i*j*k)
                exit(0)
