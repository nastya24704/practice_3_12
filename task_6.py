def opposite_definition(x):
    word = x.split(' ')
    sentence = word[::-1]
    opposite_sentence = ' '.join(sentence)
    return opposite_sentence


text = input()
print(opposite_definition(text))
