from functools import reduce


def factorial(n: int) -> int:
    """Возвращает факториал целого неотрицательного числа n."""
    if type(n) is not int:
        raise TypeError("Число должно быть целым.")
    if n < 0:
        raise ValueError("Число не должно быть отрицательным.")

    return reduce(lambda a, b: a * b, range(1, n + 1), 1)


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Введите целое неотрицательное число: "))
            print(f"{number}! = {factorial(number)}")
            break
        except ValueError:
            print("Ошибка: введите целое число не меньше нуля.")
