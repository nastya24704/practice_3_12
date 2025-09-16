text = input()
a = 0

for ch in text:
    if ch == '(':
        a += 1
    elif ch == ')':
        a -= 1
        if a < 0:
            break

if a == 0:
    print("Скобки расставлены правильно")
else:
    print("Скобки расставлены неправильно")
