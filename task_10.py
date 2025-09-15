def unique_letter(word):
    return len(word) == len(set(word))


def different_words(words):
    first_word = words[0]
    result = []
    for word in words[1:]:
        if word != first_word:
            result.append(word)
    return result


text = input()
words = text.split()
first_part = different_words(words)
result = []
for word in first_part:
    if unique_letter(word):
        result.append(word)

print(' '.join(result))
