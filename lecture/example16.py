"""Пример 16. Читаемость функционального кода."""

from __future__ import annotations

from collections.abc import Iterator


def odd_numbers(limit: int) -> Iterator[int]:
    """Выдать нечётные неотрицательные числа меньше limit."""
    return (x for x in range(limit) if x % 2)


def multiples_of_three_below(x: int) -> Iterator[int]:
    """Выдать неотрицательные кратные трём числа меньше x."""
    return (y for y in range(x) if y % 3 == 0)


def main() -> None:
    """Сверить исходное включение, именованные функции и простой цикл."""
    print("Пример 16. Читаемость")
    result = [
        x * y for x in range(10) if x % 2 for y in range(x) if y % 3 == 0 if x * y > 5
    ]
    result2 = [
        x * y for x in odd_numbers(10) for y in multiples_of_three_below(x) if x * y > 5
    ]
    print(result == result2)
    print(result2)
    expected: list[int] = []
    for x in range(10):
        for y in range(x):
            if x % 2 == 1 and y % 3 == 0 and x * y > 5:
                expected.append(x * y)
    assert result == result2 == expected == [15, 21, 42, 27, 54]
    assert list(odd_numbers(0)) == []
    assert list(odd_numbers(6)) == [1, 3, 5]
    assert list(multiples_of_three_below(7)) == [0, 3, 6]
    print("Проверки: равенство трёх реализаций, порядок, границы — OK")


if __name__ == "__main__":
    main()
