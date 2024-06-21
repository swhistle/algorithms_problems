def reverse_words_in_str(str_: str) -> str:
    words = str_.strip().split(' ')
    words_reversed = ''

    for i in range(len(words) - 1, -1, -1):
        if words[i] != '' and words[i] != ' ':
            words_reversed += ' ' + words[i]

    return words_reversed.strip()

def reverse_words_in_str_2(str_: str) -> str:
    words = str_.strip().split(' ')

    filtered_spaces_words = list(filter(lambda word: word != '', words))
    filtered_spaces_words.reverse()

    return ' '.join(filtered_spaces_words).strip()


example_1 = reverse_words_in_str('hello     world')

print(example_1)