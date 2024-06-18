def merge_two_strings(str_1: str, str_2: str) -> str:
    merged_arr = []
    max_length = max(len(str_1), len(str_2))

    for i in range(0, max_length):
        if len(str_1) > i:
           merged_arr.append(str_1[i])

        if len(str_2) > i:
           merged_arr.append(str_2[i]) 
   
    return ''.join(merged_arr)


example_1 = merge_two_strings('abc', 'pqr')
example_2 = merge_two_strings('abc', 'pqrs')
example_3 = merge_two_strings('abcd', 'pq')


print(example_1)
print(example_2)
print(example_3)