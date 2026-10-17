"""Пример 9. Списковые включения."""

from __future__ import annotations


def main() -> None:
    """Сравнить преобразование каждого элемента и фильтрацию."""
    print("Пример 9. Списковые включения")
    numbers = range(1, 11)
    squares = [n * n for n in numbers]
    even_squares = [n * n for n in numbers if n % 2 == 0]
    labels = ["чёт" if n % 2 == 0 else "нечет" for n in range(1, 6)]
    print(squares)
    print(even_squares)
    print(labels)
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert even_squares == [4, 16, 36, 64, 100]
    assert labels == ["нечет", "чёт", "нечет", "чёт", "нечет"]
    assert len(squares) == 10 and len(even_squares) == 5 and len(labels) == 5
    assert [n * n for n in []] == []
    print("Проверки: значения, фильтрация, длины, пустой вход — OK")


if __name__ == "__main__":
    main()
