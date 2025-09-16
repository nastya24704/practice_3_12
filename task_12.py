def python_name(name):
    keywords = {'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
               'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
               'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
               'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
               'try', 'while', 'with', 'yield'}
    
    if name in keywords: 
      return False
    if name[0].isdigit(): 
      return False
    
    for char in name:
        if not (char.isalpha() and char.isascii() or 
                char.isdigit() or char == '_'):
            return False
    return True

name = input().strip()
if python_name(name):
    print("Корректное имя")
else:
    print("Некорректное имя")
