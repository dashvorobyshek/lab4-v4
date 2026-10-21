def pipeline(data, *steps):
    """Последовательно передаёт результат каждого этапа следующему."""
    result = data
    for step in steps:
        result = step(result)
    return result


def keep_positive(numbers: list) -> list:
    """Возвращает список чисел, которые строго больше нуля."""
    return list(filter(lambda x: x > 0, numbers))


def square_numbers(numbers: list) -> list:
    """Возвращает список квадратов переданных чисел."""
    return list(map(lambda x: x ** 2, numbers))


def sum_numbers(numbers: list) -> int:
    """Возвращает сумму целых чисел из списка."""
    return sum(numbers)


if __name__ == "__main__":
    numbers = [-3, -1, 0, 2, 4, 5]
    result = pipeline(
        numbers,
        keep_positive,
        square_numbers,
        sum_numbers,
    )

    print("Исходный список:", numbers)
    print("Результат pipeline:", result)
    print("Без этапов:", pipeline(numbers))
    print(
        "Пустой список:",
        pipeline([], keep_positive, square_numbers, sum_numbers),
    )
