from iterators_generators import Fibo, integers, primes


def input_count() -> int:
    """
    Запрашивает количество элементов.

    :return: int
    """

    while True:
        value = input("Сколько чисел вывести? ").strip()

        try:
            count = int(value)

            if count <= 0:
                print("Ошибка! Число должно быть больше 0")
                continue

            return count

        except ValueError:
            print("Ошибка! Введите целое число")


def print_fibo(n: int):
    """
    Выводит числа Фибоначчи.

    :param n: int
    :return: None
    """

    fib = Fibo()

    print("\nЧисла Фибоначчи:")

    for _ in range(n):
        print(next(fib))


def print_integers(n: int):
    """
    Выводит целые числа.

    :param n: int
    :return: None
    """

    gen = integers()

    print("\nЦелые числа:")

    for _ in range(n):
        print(next(gen))


def print_primes(n: int):
    """
    Выводит простые числа.

    :param n: int
    :return: None
    """

    gen = primes()

    print("\nПростые числа:")

    for _ in range(n):
        print(next(gen))


def run():
    """
    Основной запуск программы.

    :return: None
    """

    try:
        count = input_count()

        print_fibo(count)
        print_integers(count)
        print_primes(count)

    except Exception as e:
        print("Ошибка:", e)