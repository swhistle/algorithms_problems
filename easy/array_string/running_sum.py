def running_sum(nums: list) -> list:
    result = []
    for (index, item) in enumerate(nums):
        if index > 0:
            result.append(nums[index] + result[index - 1])
        else:
            result.append(nums[index])

    return result


print(running_sum([1, 2, 3, 4, 5]))
print(running_sum([1, 1, 1, 1, 1]))