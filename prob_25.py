value = 1
index = 100
ALOT = 10**999

n1, n2 = 1, 1
count = 2
while n1 < ALOT and n2 < ALOT:
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1

print(count)
