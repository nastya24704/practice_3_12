def all_bulls_cows(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def play_game():
    secret = num
    print("\n" * 25)
    attempts = 10
    print("Игра началась! Отгадайте число за 10 попыток.")
    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Попытка {attempt}. Введите ваш вариант: ")
            if len(guess) == 4 and len(set(guess)) == 4:
                break
            print("Введите четырехзначное число с неповторяющимися цифрами.")

        if guess == secret:
            print("Победа!")
            return
        bulls, cows = all_bulls_cows(secret, guess)
        print(f"Быков: {bulls} Коров: {cows}")

    print(f"Проигрыш! Загаданное число было: {secret}")
num=input()


play_game()
