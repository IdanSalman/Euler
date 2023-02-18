import math


def find_rec(str_num):
    row_of_zeros = True
    temp_str = ""
    count = 0
    while True:
        temp_str += str_num[count]
        count += 1
        length_of_string = len(temp_str)
        if str_num[count] != "0":
            row_of_zeros = False
        if row_of_zeros:
            continue
        if str_num.find(temp_str, length_of_string) != -1:
            if str_num.find(temp_str, length_of_string) == length_of_string:
                return temp_str


def rec_frac(num):
    count = 0
    if len(str(num)) == 3:
        start_str = "00"
        start_str += str(int(1000 / num))
        remainder = 1000 % num
    elif len(str(num)) == 2:
        start_str = "0"
        start_str += str(int(100 / num))
        remainder = 100 % num
    elif len(str(num)) == 1:
        start_str = str(int(10 / num))
        remainder = 10 % num

    if remainder == 0:
        return start_str
    i = 0
    while count < 10000:
        if int(remainder * 10**i / num) == 0:
            i += 1
        else:
            for _ in range(i - 1):
                start_str += "0"
            start_str += str(int(remainder * 10**i / num))
            remainder = remainder * 10**i % num
            if remainder == 0:
                return ""
            i = 0
            count += 1
    return find_rec(start_str)


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    prime_list = []
    # The number must be a prime number
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
