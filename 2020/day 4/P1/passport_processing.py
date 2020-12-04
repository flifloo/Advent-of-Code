print(
    len(
        list(
            filter(
                lambda x: all(y in [e[1] for e in x] for y in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]),
                map(
                    lambda x: __import__("re").findall(r"((byr|iyr|eyr|hgt|hcl|ecl|pid|cid):([a-zA-Z0-9#]+))", x),
                    [m.replace("\n", " ") for m in open("input.txt").read().split("\n\n")]
                )
            )
        )
    )
)
