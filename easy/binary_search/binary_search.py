def binary_search(nums: list, target: int) -> int:
    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left_i = 0
    right_i = len(nums) - 1
    middle_i = (left_i + right_i) // 2

    while left_i <= right_i - 1:
        if target == nums[left_i]:
            return left_i
        elif target == nums[right_i]:
            return right_i
        elif target == nums[middle_i]:
            return middle_i
        elif target < nums[middle_i]:
            right_i = middle_i - 1
            middle_i = (left_i + right_i) // 2
        elif target > nums[middle_i]:
            left_i = middle_i + 1
            middle_i = (left_i + right_i) // 2

    return -1


nums_1 = [-1, 0, 3, 5, 9, 12]

for i in range(0, 15):
    target = i
    result = binary_search(nums_1, target)
    print('nums_1', nums_1, 'target', target, 'position', result)


nums_2 = [5]
target_2 = 5
result_2 = binary_search(nums_2, target_2)
print('nums_2', nums_2, 'target', target_2, 'position', result_2)

nums_3 = [1, 5]
target_3 = 5
result_3 = binary_search(nums_3, target_3)
print('nums_3', nums_3, 'target', target_3, 'position', result_3)
