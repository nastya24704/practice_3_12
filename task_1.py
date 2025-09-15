def space(x):
    max_count = 0
    count = 0
    for ch in x:
        if ch == ' ':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    return max_count


text = input()
print(space(text))
