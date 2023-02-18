import requests as req

x = req.get("https://projecteuler.net/project/resources/p022_names.txt")

all_names = x.text.split(",")

all_names.sort()

total_sum = 0

for i, name in enumerate(all_names):
    for letter in name:
        if letter == '"':
            continue
        total_sum += (i + 1) * (ord(letter) - 64)

print(total_sum)
