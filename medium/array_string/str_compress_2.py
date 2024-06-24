def str_compress(chars: list) -> int:
    last_char_cached = ''
    compressed = []

    for i in range(0, len(chars)):
        if chars[i] == last_char_cached:
            if chars[i] == compressed[-1]:
                compressed.append(2)
            elif isinstance(compressed[-1], int):
                compressed[-1] += 1
        else:
            last_char_cached = chars[i]
            compressed.append(chars[i])

    compressed = list(map(lambda x: str(x), compressed))
    compressed = ''.join(compressed)

    len_compressed = len(compressed)

    for i in range(0, len(chars)):
        if i < len_compressed:
            chars[i] = compressed[i]
        else:
            chars[i] = '#'

    n_chars_for_delete = len(chars) - len_compressed

    for i in range(n_chars_for_delete):
        chars.pop(-1)

    return len_compressed


arr_1 = ['a', 'a', 'a', 'a', 'a', 'a', 'b']
arr_2 = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c']
arr_3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

res = str_compress(arr_1)
res_2 = str_compress(arr_2)
res_3 = str_compress(arr_3)

print(arr_1, res)
print(arr_2, res_2)
print(arr_3, res_3)