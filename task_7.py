def min_word(x):
    words = x.split()
    return min(len(word) for word in words)


text = input()
print(min_word(text))
