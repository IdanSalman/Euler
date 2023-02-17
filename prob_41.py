import math


def is_prime(num):
    for i in range(2, int(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            return False
    return True


def is_pand(num):
    str_num = str(num)
    for i in range(1, 10):
        if str(i) not in str_num:
            return False
    return True


if __name__ == "__main__":
    max_num = 0
    for i in range(10**8, 10**9):
        if is_pand(i):
            if is_prime(i):
                if i > max_num:
                    max_num = i
    # Works but takes way too long
    print(max_num)
