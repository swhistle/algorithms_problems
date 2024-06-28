def search_insert_position(nums: list, target) -> int:
    left_index = 0
    right_index = len(nums) - 1
    middle_index = (left_index + right_index) // 2
    middle_next_index = middle_index + 1

    if right_index < 1:
        return 0 if target <= nums[left_index] else 1

    while left_index <= right_index - 1:
        if target > nums[right_index]:
            return right_index + 1
        elif target <= nums[left_index]:
            return left_index
        elif target > nums[middle_index] and target <= nums[middle_next_index]:
            return middle_next_index
        elif target > nums[middle_index] and target >= nums[middle_next_index]:
            left_index = middle_next_index
        elif target <= nums[middle_index]:
            right_index = middle_index

        middle_index = (left_index + right_index) // 2
        middle_next_index = middle_index + 1

    return middle_next_index



nums_1 = [1, 3, 5, 6]

for i in range(0, 10):
    target = i
    result = search_insert_position(nums_1, target)
    print('nums_1', nums_1, 'target', target, 'position', result)



nums_2 = [1,3]
target_2 = 4
result_2 = search_insert_position(nums_2, target_2)
print('nums_2', nums_2, 'target', target_2, 'position', result_2)
