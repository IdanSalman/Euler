import math


def div_sum(num: int):
    sum = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            sum += i + num / i
    return int(sum) - num


if __name__ == "__main__":
    sum = 0
    num_map = {}
    for i in range(2, 10000):
        if i in num_map.keys():
            curr_amount = num_map[i]
        else:
            curr_amount = div_sum(i)
            num_map[i] = curr_amount
        if curr_amount == i:
            continue
        if curr_amount in num_map.keys():
            if i == num_map[curr_amount]:
                sum += i + curr_amount
        else:
            other_sum = div_sum(curr_amount)
            num_map[curr_amount] = other_sum
            if other_sum == i:
                sum += i + curr_amount
    print(sum / 2)  # We sum the amicable numbers twice
