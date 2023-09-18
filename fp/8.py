from functools import reduce


def find_max_and_second_max(max_nums, num):
    if num > max_nums[0]:
        return [num, max_nums[0]]
    elif num > max_nums[1]:
        return [max_nums[0], num]
    else:
        return max_nums


numbers = [3, 2.6, 7, 2.8, 4, 3, 2, 5, 7]

print(reduce(find_max_and_second_max, numbers, [float('-inf'), float('-inf')])[1])
