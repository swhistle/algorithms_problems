def kids_with_candies(candies: list[int], extra_candies: int) -> list[bool]:
    max_candies_number = max(candies)

    result = list(map(lambda x: x + extra_candies >= max_candies_number, candies))

    return result


candies_1 = [2,3,5,1,3]
extra_candies_1 = 3
res_1 = kids_with_candies(candies_1, extra_candies_1)
print(res_1)

candies_2 = [4,2,1,1,2]
extra_candies_2 = 1
res_2 = kids_with_candies(candies_2, extra_candies_2)
print(res_2)