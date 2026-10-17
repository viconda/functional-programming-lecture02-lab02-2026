"""Задание 3. Десять отдельных решений включениями."""

import sys
from math import isqrt


def odd_squares() -> list[int]:
    """Получить квадраты нечётных чисел от 1 до 30 включительно."""
    return [number**2 for number in range(1, 31) if number % 2 != 0]


def multiplication_table() -> list[list[int]]:
    """Построить таблицу умножения для индексов от 1 до 5."""
    return [[i * j for j in range(1, 6)] for i in range(1, 6)]


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Транспонировать прямоугольную матрицу; пустая даёт []."""
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))] if matrix else []


def flatten(rows: list[list[int]]) -> list[int]:
    """Развернуть один уровень вложенности списка."""
    return [value for row in rows for value in row]


def word_lengths(sentence: str) -> dict[str, int]:
    """Убрать крайние знаки препинания и измерить слова от 3 букв."""
    return {
        word: len(word)
        for token in sentence.split()
        if len(word := token.strip(".,!?;:")) >= 3
    }


def invert_groups(data: dict[str, int]) -> dict[int, list[str]]:
    """Сгруппировать все исходные ключи по их значениям."""
    return {
        value: [key for key, item in data.items() if item == value]
        for value in data.values()
    }


def vowels(text: str) -> set[str]:
    """Получить русские и латинские гласные без учёта регистра."""
    return {char for char in text.lower() if char in "аеёиоуыэюяaeiou"}


def pythagorean_triples() -> list[tuple[int, int, int]]:
    """Найти все, включая непримитивные, тройки a < b < c <= 50."""
    return [
        (a, b, c)
        for a in range(1, 51)
        for b in range(a + 1, 51)
        for c in range(b + 1, 51)
        if a * a + b * b == c * c
    ]


def primes() -> list[int]:
    """Найти простые числа до 100 проверкой делителей до корня."""
    return [
        number
        for number in range(2, 101)
        if all(number % divisor for divisor in range(2, isqrt(number) + 1))
    ]


def uppercase_positions(text: str) -> list[tuple[int, str]]:
    """Вернуть индексы с нуля и символы всех заглавных букв."""
    return [(index, char) for index, char in enumerate(text) if char.isupper()]


def digit_sum() -> int:
    """Сложить цифры всех чисел от 1 до 1000 включительно."""
    return sum(int(digit) for number in range(1, 1001) for digit in str(number))


def main(part: str) -> None:
    """Выполнить выбранный подпункт и проверить его результат."""
    print(f"Задание 3, подпункт {part}")
    if part == "1":
        result = odd_squares()
        print("Вход: целые числа от 1 до 30, нужны нечётные.")
        assert result == [
            1,
            9,
            25,
            49,
            81,
            121,
            169,
            225,
            289,
            361,
            441,
            529,
            625,
            729,
            841,
        ]
    elif part == "2":
        source = multiplication_table()
        result = transpose(source)
        print("Матрица 5x5, i и j от 1 до 5:", source)
        print("Транспонирование дважды восстанавливает исходную матрицу.")
        assert transpose(result) == source
        assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
        assert result == source and result is not source
    elif part == "3":
        source = [[1, 2], [3], [], [4, 5, 6]]
        result = flatten(source)
        print("Вход:", source)
        assert result == [1, 2, 3, 4, 5, 6]
        assert source == [[1, 2], [3], [], [4, 5, 6]]
    elif part == "4":
        source = "Мы изучаем Python и пишем чистые функции."
        result = word_lengths(source)
        print("Предложение:", source)
        assert result == {
            "изучаем": 7,
            "Python": 6,
            "пишем": 5,
            "чистые": 6,
            "функции": 7,
        }
    elif part == "5":
        source = {"a": 1, "b": 2, "c": 1}
        result = invert_groups(source)
        print("Вход:", source)
        assert result == {1: ["a", "c"], 2: ["b"]}
        assert source == {"a": 1, "b": 2, "c": 1}
    elif part == "6":
        source = "Функциональное ПРОГРАММИРОВАНИЕ, Python, Ёж!"
        result = sorted(vowels(source))
        print("Текст:", source)
        assert set(result) == set("аеёиоуo")
    elif part == "7":
        result = pythagorean_triples()
        print("Условие: целые положительные a < b < c <= 50")
        print("Количество троек:", len(result))
        assert len(result) == 20
        assert all(a < b < c <= 50 and a * a + b * b == c * c for a, b, c in result)
        assert len(result) == len(set(result))
    elif part == "8":
        result = primes()
        print("Вход: числа от 2 до 100; делители до целого корня.")
        assert result == [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
    elif part == "9":
        source = "Python и SQL: АбВ!"
        result = uppercase_positions(source)
        print("Строка:", source, "| индексы с нуля")
        assert result == [
            (0, "P"),
            (9, "S"),
            (10, "Q"),
            (11, "L"),
            (14, "А"),
            (16, "В"),
        ]
    elif part == "10":
        result = digit_sum()
        print("Вход: цифры всех целых чисел от 1 до 1000.")
        assert result == 13501
    else:
        raise ValueError("Подпункт должен быть от 1 до 10")
    print("Результат:", result)
    print("Проверка: все assert выполнены; аккумуляторы не используются.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1")
