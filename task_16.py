text = input()
balance = 0

for ch in text:
    if ch == '(':
        balance += 1
    elif ch == ')':
        balance -= 1
        if balance < 0:
            break

if balance == 0:
    print("Скобки расставлены правильно")
else:
    print("Скобки расставлены неправильно")
