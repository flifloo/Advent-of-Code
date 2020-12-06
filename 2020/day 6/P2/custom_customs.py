qs = []

with open("input.txt") as f:
    for q in f.read().split("\n\n"):
        s = {}
        q = list(filter(lambda x: x, q.split("\n")))
        ln = len(q)
        for a in q:
            for le in list(a):
                s[le] = s[le] + 1 if le in s else 1
        qs.append(list(filter(lambda x: s[x] == ln, s)))

print(sum(map(lambda x: len(x), qs)))
