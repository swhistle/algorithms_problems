def reverse_vowels_of_str(str_: str) -> str:
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    str_vowels = []
    result = []

    for i in range(len(str_)):
        if str_[i] in vowels:
            str_vowels.append(str_[i])

    for i in range(len(str_)):
        if str_[i] in vowels:
            result.append(str_vowels.pop())
        else:
            result.append(str_[i])

    return ''.join(result)


example_1 = reverse_vowels_of_str('hello')
example_2 = reverse_vowels_of_str('leetcode')
example_3 = reverse_vowels_of_str('mgmt')
example_4 = reverse_vowels_of_str('AAEEIOIU')

print(example_1)
print(example_2)
print(example_3)
print(example_4)