def str_compress(chars: list) -> int:
    if len(chars) < 2:
        return len(chars)

    i = 0
    j = 1
    compressed_str = []
    char_counter = 1

    while i < len(chars):
        if j < len(chars):
            if chars[j] == chars[i]:
                char_counter += 1
                j += 1
            else:
                compressed_str.append(chars[i])

                if char_counter > 1:
                    for digit in str(char_counter):
                        compressed_str.append(digit)

                char_counter = 1
                i = j
                j = j + 1
        else:
            compressed_str.append(chars[i])

            if char_counter > 1:
                for digit in str(char_counter):
                    compressed_str.append(digit)

            break

    for i in range(len(compressed_str)):
        chars[i] = compressed_str[i]

    n_chars_for_delete = len(chars) - len(compressed_str)

    for j in range(n_chars_for_delete):
        chars.pop()


    return len(chars)




arr_1 = ['a', 'a', 'a', 'a', 'a', 'a', 'b']
arr_2 = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
arr_3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

res = str_compress(arr_1)
res_2 = str_compress(arr_2)
res_3 = str_compress(arr_3)

print(arr_1, res)
print(arr_2, res_2)
print(arr_3, res_3)