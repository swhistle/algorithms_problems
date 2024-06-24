def merge_two_strings(str_1: str, str_2: str) -> str:
    merged_str = ''
    i = 0
    j = 0

    while i < len(str_1) and j < len(str_2):
        merged_str += str_1[i] + str_2[j]
        i += 1
        j += 1

    if i < len(str_1):
        merged_str += str_1[i:]

    if j < len(str_2):
        merged_str += str_2[j:]

    return merged_str


example_1 = merge_two_strings('abc', 'pqr')
example_2 = merge_two_strings('abc', 'pqrs')
example_3 = merge_two_strings('abcd', 'pq')


print(example_1)
print(example_2)
print(example_3)