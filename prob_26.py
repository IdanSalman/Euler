import math


def close_to(a, b):
    return abs(a - b) < 10**-5


def rec_frac(num):
    # ! Fuck this bullshit
    pass


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    prime_list = []
    for i in range(2, 1000):
        if is_prime(i):
            prime_list.append(i)

    max_len = 0
    max_num = 0

    for prime_number in prime_list:
        length_of_frac = len(rec_frac(prime_number))
        if length_of_frac > max_len:
            max_len = length_of_frac
            max_num = prime_number

    print(max_num)
