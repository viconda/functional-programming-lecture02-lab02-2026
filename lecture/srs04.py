"""СРС 4. Встроенные функции в параметре key."""

from __future__ import annotations


def main() -> None:
    """Показать len, abs и str.lower в sorted, min и max."""
    print("СРС 4. Параметр key")
    words = ["map", "filter", "zip", "lambda", "a"]
    by_length = sorted(words, key=len)
    print("sorted(key=len):", by_length)
    numbers = [-8, 3, -2, 5]
    nearest_zero = min(numbers, key=abs)
    print("min(key=abs):", nearest_zero)
    names = ["Анна", "борис", "Вера"]
    alphabetic_max = max(names, key=str.lower)
    print("max(key=str.lower):", alphabetic_max)
    assert by_length == ["a", "map", "zip", "filter", "lambda"]
    assert nearest_zero == -2 and alphabetic_max == "Вера"
    assert words == ["map", "filter", "zip", "lambda", "a"]
    assert min([-2, 2], key=abs) == -2
    assert max(["А", "а"], key=str.lower) == "А"
    assert sorted(["Ab", "aB", "AA"], key=str.lower) == ["AA", "Ab", "aB"]
    assert min([], key=abs, default=None) is None
    print("Равные ключи: сохраняется первый элемент или исходный порядок")
    print("Проверки: 3 встроенных key, стабильность, равные ключи, пустой вход — OK")


if __name__ == "__main__":
    main()
