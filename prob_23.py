import math


def div_sum(num: int):
    sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i
            temp = num / i
            if i != temp:
                sum += temp
    return int(sum)


def number_type(num: int):
    div_summary = div_sum(num)
    if div_summary > num:
        return "Abundant Number"
    elif div_summary == num:
        return "Perfect Number"
    return "Deficient Number"


if __name__ == "__main__":
    # ? IMPORTANT Dictionary is WAY MORE efficient than a list
    abundant_nums = {}
    for i in range(12, 28123):
        if number_type(i) == "Abundant Number":
            abundant_nums[i] = "0"

    sum = 0
    Found = False
    for i in range(1, 28124):
        for j in abundant_nums:
            if i - j in abundant_nums.keys():
                Found = True
                break
        if not Found:
            sum += i
        Found = False
    print(sum)
