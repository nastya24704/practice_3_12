def find_similar(x):
    words = x.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i] == words[j]:
                return words[i]

text = input()
print(find_similar(text))
