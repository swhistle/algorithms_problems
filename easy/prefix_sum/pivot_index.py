def pivot_index(nums: list) -> int:
    result = -1
    left_sum = nums[0]
    right_sum = sum(nums)

    if right_sum == left_sum:
        result = 0
        print(result)
        return result

    for i in range(1, len(nums)):
        left_sum += nums[i]
        right_sum -= nums[i - 1]

        if left_sum == right_sum:
            result = i
            break

    print(result)
    return result


arr1 = [1, 7, 3, 6, 5, 6]
arr2 = [1, 2, 3]
arr3 = [2, 1, -1]
arr4 = [2, 1, 0, 0, 3]
pivot_index(arr1)
pivot_index(arr2)
pivot_index(arr3)
pivot_index(arr4)
