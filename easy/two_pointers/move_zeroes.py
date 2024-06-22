def move_zeroes(nums: list) -> None:
    i = 0
    j = 1

    while i <= len(nums) - 1 and j <= len(nums) - 1:
        # print('i', i, 'j', j, 'nums', nums)

        if nums[i] == 0:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                j += 1
        else:
            i += 1

        if j < i:
            j = i + 1


def move_zeroes_square(nums: list) -> None:
    for i in range(0, len(nums) - 1):
        if nums[i] == 0:
            j = i + 1

            while (j < len(nums) - 1) and nums[j] == 0:
                j += 1

            nums[i], nums[j] = nums[j], nums[i]


def move_zeroes_pop_append(nums: list) -> None:
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            zero = nums.pop(i)
            nums.append(zero)


nums_1 = [0,1,0,3,12]
print(nums_1)
move_zeroes(nums_1)
print(nums_1, '\n')

nums_2 = [0,0,1]
print(nums_2)
move_zeroes(nums_2)
print(nums_2, '\n')

nums_3 = [0,0,1,1,1]
print(nums_3)
move_zeroes(nums_3)
print(nums_3, '\n')

nums_4 = [4,2,4,0,0,3,0,5,1,0]
print(nums_4)
move_zeroes(nums_4)
print(nums_4)
