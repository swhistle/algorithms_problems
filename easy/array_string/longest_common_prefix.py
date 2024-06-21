def longest_common_prefix(strs: list) -> str:
    if len(strs) < 1:
        return ''

    common_prefix = ''

    min_word_len = len(strs[0])
    min_word_index = 0

    for i in range(1, len(strs)):
        if len(strs[i]) < min_word_len:
            min_word_len = len(strs[i])
            min_word_index = i

    for i in range(0, min_word_len):
        new_prefix = common_prefix + strs[min_word_index][i]
        is_common = all(map(lambda word: new_prefix == word[0:len(new_prefix)], strs))
        if is_common:
            common_prefix = new_prefix

    print(common_prefix)
    return common_prefix



strs = ["flower","flow","flight"]
res_1 = longestCommonPrefix(strs)

strs_2 = ["dog","racecar","car"]
res_2 = longestCommonPrefix(strs_2)

strs_3 = ["refl","flowflow","flightflight"]
res_3 = longestCommonPrefix(strs_3)