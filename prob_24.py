import math
import numpy as np

POSITION = 1_000_000
NUM_AMOUNT = 10


def calc_fac(str_num):
    seen_num = []
    amount = len(str_num)
    sum = 0
    for i in range(amount):
        count = 0
        for num in seen_num:
            if int(str_num[i]) > num:
                count += 1
        sum += (int(str_num[i]) - count) * math.factorial(amount - i - 1)
        seen_num.append(int(str_num[i]))
    return sum


def swap(s, i, j):
    return "".join((s[:i], s[j], s[i + 1 : j], s[i], s[j + 1 :]))


def swap_ind(str_num: str, index: int):
    temp = int(str_num[index])
    next_index = str_num[index:].find(str(temp + 1))
    count = 1
    while next_index == -1:
        count += 1
        next_index = str_num[index:].find(str(temp + count))
    return swap(str_num, index, next_index + index)


def swap_back(str_num: str, index: int):
    temp = int(str_num[index])
    previous_index = str_num[index:].find(str(temp - 1))
    count = 1
    while previous_index == -1:
        count += 1
        previous_index = str_num[index:].find(str(temp - count))
    return swap(str_num, index, previous_index + +index)


if __name__ == "__main__":
    ans_perm = "9876543210"
    sum = 0
    curr_pos = 0
    while sum != POSITION - 1:
        for i in range(1, 10):
            sum = calc_fac(ans_perm)
            if sum > POSITION - 1 and ans_perm[curr_pos] != "0":
                ans_perm = swap_back(ans_perm, curr_pos)
            elif sum == POSITION - 1:
                break
            else:
                if ans_perm[curr_pos] != "9":
                    ans_perm = swap_ind(ans_perm, curr_pos)
                curr_pos += 1
                break
    print(ans_perm)
