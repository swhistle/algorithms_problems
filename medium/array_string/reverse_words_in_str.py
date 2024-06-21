def reverse_words_in_str(str_: str) -> str:
    words = str_.strip().split(' ')
    filtered_spaces_words = list(filter(lambda word: word != '', words))
    print(filtered_spaces_words)
    filtered_spaces_words.reverse()
    return ' '.join(filtered_spaces_words).strip()


example_1 = reverse_words_in_str('hello     world')

print(example_1)