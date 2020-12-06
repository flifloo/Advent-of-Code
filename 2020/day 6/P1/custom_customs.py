qs = []

with open("input.txt") as f:
    for q in f.read().split("\n\n"):
        s = set()
        for a in q.split("\n"):
            s.update(list(a))
        qs.append(s)

print(sum(map(lambda x: len(x), qs)))
