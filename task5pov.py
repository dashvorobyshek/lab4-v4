class SquareIterator:
    """Выдаёт квадраты чисел от 1 до limit включительно."""

    def __init__(self, limit: int):
        """Проверяет границу и устанавливает начальное состояние."""
        if type(limit) is not int:
            raise TypeError("Граница должна быть целым числом.")
        if limit < 0:
            raise ValueError("Граница не должна быть отрицательной.")

        self.limit = limit
        self.current = 1

    def __iter__(self):
        """Возвращает сам итератор без сброса состояния."""
        return self

    def __next__(self) -> int:
        """Возвращает следующий квадрат или вызывает StopIteration."""
        if self.current > self.limit:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


if __name__ == "__main__":
    iterator = SquareIterator(5)

    print("Первый элемент:", next(iterator))
    print("Оставшиеся элементы:", list(iterator))
    print("После завершения:", list(iterator))
    print("При нулевой границе:", list(SquareIterator(0)))
