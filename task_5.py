def unique_symbols(x, y, z):
    all_s = set(x+y+z)
    unique_s = []
    for ch in all_s:
        count = 0
        if ch in x:
            count += 1
        if ch in y:
            count += 1
        if ch in z:
            count += 1
        if count == 1:
            unique_s.append(ch)
    return unique_s


first = input()
second = input()
third = input()
print(''.join(unique_symbols(first, second, third)))
