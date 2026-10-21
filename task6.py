def prime_numbers(limit: int):
    """Выдаёт простые числа от 2 до limit включительно."""
    if type(limit) is not int:
        raise TypeError("Граница должна быть целым числом.")
    if limit < 0:
        raise ValueError("Граница не должна быть отрицательной.")

    for number in range(2, limit + 1):
        is_prime = True
        divisor = 2

        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            yield number


if __name__ == "__main__":
    while True:
        try:
            limit = int(input("Введите целую неотрицательную границу: "))
            print("Простые числа:", list(prime_numbers(limit)))
            break
        except ValueError:
            print("Ошибка: введите целую границу не меньше нуля.")
