class Fibo:
    """
    Итератор для чисел Фибоначчи.
    """

    def __init__(self):
        """
        Инициализация последовательности.

        :return: None
        """

        self.a = 0
        self.b = 1

    def __iter__(self):
        """
        Возвращает итератор.

        :return: Fibo
        """

        return self

    def __next__(self):
        """
        Возвращает следующее число Фибоначчи.

        :return: int
        """

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


def integers():
    """
    Генератор неотрицательных целых чисел.

    :yield: int
    """

    num = 0

    while True:
        yield num
        num += 1


def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым.

    :param n: int
    :return: bool
    """

    if n <= 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def primes():
    """
    Генератор простых чисел.

    :yield: int
    """

    num = 2

    while True:
        if is_prime(num):
            yield num
        num += 1