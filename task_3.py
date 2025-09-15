def symbol(x):
    unique_l = set()
    for i in x.lower():
        if i.isalpha():
            unique_l.add(i)
    return len(unique_l)


text = input()
print(symbol(text))
