def winner(city):
    cities = city.split()

    for i in range(1, len(cities)):
        previous_city = cities[i - 1].lower()
        current_city = cities[i].lower()

        last_char = last_letter(previous_city)

        if current_city[0] != last_char:
            if i % 2 == 1:
                return "Петя"
            else:
                return "Вася"

    if len(cities) % 2 == 1:
        return "Петя"
    else:
        return "Вася"


def last_letter(city):
    excluded_chars = {'ь', 'ъ', 'ы'}

    for i in range(len(city) - 1, -1, -1):
        if city[i] not in excluded_chars:
            return city[i]
    return city[-1]


cities_input = input().strip()
winner = winner(cities_input)
print(f"Победитель: {winner}")
