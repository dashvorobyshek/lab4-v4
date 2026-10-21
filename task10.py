def apply_functions(numbers: list, functions: list) -> list:
    """Возвращает отдельный список результатов для каждой функции."""
    return [list(map(function, numbers)) for function in functions]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    functions = [
        lambda x: x ** 2,
        lambda x: x * 2,
        lambda x: x + 1,
    ]
    names = ["Квадраты", "Удвоение", "Прибавление единицы"]
    results = apply_functions(numbers, functions)

    print("Исходный список:", numbers)
    for name, result in zip(names, results):
        print(f"{name}: {result}")
