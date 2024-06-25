def romanToInt(str: str) -> int:
    roman_digits_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_digits_counter = {
        'I': 0,
        'V': 0,
        'X': 0,
        'L': 0,
        'C': 0,
        'D': 0,
        'M': 0
    }

    for i in range(0, len(str) - 1):
        current_digit = roman_digits_dict[str[i]]
        next_digit = roman_digits_dict[str[i + 1]]

        if current_digit >= next_digit:
            roman_digits_counter[str[i]] += 1
        elif current_digit < next_digit:
            roman_digits_counter[str[i]] -= 1
        else:
            raise Exception('Wrong input roman number')

    # Count last roman digit because it was not counted in loop
    roman_digits_counter[str[-1]] += 1

    decimal_number = 0

    for roman_digit in roman_digits_counter.keys():
        n_roman_digits = roman_digits_counter[roman_digit]
        roman_digit_value = roman_digits_dict[roman_digit]

        decimal_number += roman_digit_value * n_roman_digits

    print(f'{str} is equal to {decimal_number}')
    return decimal_number


roman_num_1 = 'III'
roman_num_2 = 'LVIII'
roman_num_3 = 'MCMXCIV'

result_1 = romanToInt(roman_num_1)
result_2 = romanToInt(roman_num_2)
result_3 = romanToInt(roman_num_3)


