def str_common_divisor(str_1: str, str_2: str) -> str:
    common_divisor = ''
    short_str = ''
    long_str = ''

    if len(str_1) <= len(str_2):
        short_str = str_1
        long_str = str_2
    else:
        short_str = str_2
        long_str = str_1


    for i in range(len(short_str)):
        sub_str = short_str[0 : i + 1]

        multiplier_1 = len(short_str) // len(sub_str)
        multiplier_2 = len(long_str) // len(sub_str)

        if short_str == sub_str * multiplier_1 and long_str == sub_str * multiplier_2:
            common_divisor = sub_str


    return common_divisor


example_1 = str_common_divisor('ABCABC', 'ABC')
example_2 = str_common_divisor('ABABAB', 'ABC')
example_3 = str_common_divisor('ABABAB', 'ABAB')
example_4 = str_common_divisor('ABABAB', 'CDCD')
example_5 = str_common_divisor('ABCDABCD', 'ABCDABCD')
example_6 = str_common_divisor('ABABAB', '')


print(example_1)
print(example_2)
print(example_3)
print(example_4)
print(example_5)
print(example_6)

