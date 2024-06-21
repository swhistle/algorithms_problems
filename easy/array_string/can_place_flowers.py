from typing import List

def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True

    if len(flowerbed) == 1 and flowerbed[0] == 0:
        return True

    flowers_for_planting = [1] * n

    for i in range(len(flowerbed)):
        if len(flowers_for_planting) == 0:
            break
        # start of flowerbed
        if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = flowers_for_planting.pop()

        # end of flowerbed
        if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
            flowerbed[i] = flowers_for_planting.pop()

        # middle of flowerbed
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = flowers_for_planting.pop()

    return len(flowers_for_planting) == 0



print(can_place_flowers([0, 0, 1], 2))
print(can_place_flowers([1,0,0,0,0,0,0,1], 1))
print(can_place_flowers([1,0,0,0,1], 2))
print(can_place_flowers([0], 1))
print(can_place_flowers([0, 1], 1))