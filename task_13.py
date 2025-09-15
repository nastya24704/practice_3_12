def lucky_ticket(ticket):
    length = len(ticket)
    if length % 2 != 0:
        return False

    half = length // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    sum_first = sum(int(d) for d in first_half)
    sum_second = sum(int(d) for d in second_half)
    if sum_first == sum_second:
        return True
    else:
        return False


def find_luck():
    count = 0
    while True:
        ticket = input("Введите номер билета: ").strip()
        count += 1
        if lucky_ticket(ticket):
            print(f"Вы нашли счастливый билет! Его порядковый номер: {count}")
            break

find_luck()
