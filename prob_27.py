import math


def is_prime(num):
    for i in range(2, int(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = 0
    # formula = n**2 + a * n + b

    count = 0
    max_count = 0
    max_a = 0
    max_b = 0
    prime_list = []
    num_found = False
    for i in range(2, 1000):
        if is_prime(i):
            prime_list.append(i)

    for a in range(1, 1000):
        for b in prime_list:
            while not num_found:
                formula = n**2 + a * n + b
                if is_prime(formula):
                    count += 1
                    n += 1
                else:
                    num_found = True
            if count > max_count:
                max_count = count
                max_a = a
                max_b = b
            num_found = False
            count = 0
            n = 0

    for a in range(1, 1000):
        for b in prime_list:
            while not num_found:
                formula = n**2 - a * n + b
                if formula < 2:
                    num_found = True
                if is_prime(formula):
                    count += 1
                    n += 1
                else:
                    num_found = True
            if count > max_count:
                max_count = count
                max_a = -a
                max_b = b
            num_found = False
            count = 0
            n = 0
    print(max_a * max_b)
