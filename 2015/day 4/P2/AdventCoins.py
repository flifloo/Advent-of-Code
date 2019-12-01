import hashlib
key = open("input.txt").read().replace("\n", "")
num=0
while hashlib.md5(f"{key}{num}".encode()).hexdigest()[:6] != "000000":
    num+=1
print(num)
