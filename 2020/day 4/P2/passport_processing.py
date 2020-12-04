print(
    len(
        list(
            filter(
                lambda x: x and len(x) == 7,
                map(
                    lambda x: __import__("re").findall(r"(?:(?:byr:(?:19[2-9][0-9]|200[0-2])|iyr:(?:201[0-9]|2020)|eyr:(?:202[0-9]|2030)|hgt:(?:1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)|hcl:#[0-9a-f]{6}|ecl:(?:amb|blu|brn|gry|grn|hzl|oth)|pid:[0-9]{9})(?: |$))", x),
                    [m.replace("\n", " ") for m in open("input.txt").read().split("\n\n")]
                )
            )
        )
    )
)
