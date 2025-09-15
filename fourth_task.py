def symbol(x):
    for ch in x:
        if x.count(ch)==3:
            return ch


text = input()
print(symbol(text))
