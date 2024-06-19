def two_sum(nums: list, target: int) -> list:
    current = {
        'value': None,
        'index': None
    }

    for i in range(0, len(nums)):
        current['value'] = nums[i]
        current['index'] = i

        for j in range(i + 1, len(nums)):
            if current['value'] + nums[j] == target:
                return [current['index'], j]
    return []


example_1_nums = [2,7,11,15]
example_1_target = 9
res_1 = two_sum(example_1_nums, example_1_target)
print(res_1)

example_2_nums = [3,2,4]
example_2_target = 6
res_2 = two_sum(example_2_nums, example_2_target)
print(res_2)

example_3_nums = [3,3]
example_3_target = 6
res_3 = two_sum(example_3_nums, example_3_target)
print(res_3)