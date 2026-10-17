"""Пример 6. Логические выражения."""

from __future__ import annotations


def main() -> None:
    """Проверить возвращаемые операнды и короткое замыкание."""
    print("Пример 6. and и or")
    name = ""
    display = name or "Гость"
    print(display)
    print(0 and 5, 3 and 5, None or 7)
    assert display == "Гость"
    assert (0 and 5) == 0 and (3 and 5) == 5 and (None or 7) == 7
    assert ("Алия" or "Гость") == "Алия"
    assert (False and (1 / 0)) is False
    assert (True or (1 / 0)) is True
    value = 0
    preserved = value if value is not None else 7
    assert preserved == 0 and (value or 7) == 7
    print("Короткое замыкание: деление на ноль не выполняется")
    print("0 or 7 =", value or 7, "; проверка is not None сохраняет", preserved)
    print("Проверки: операнды, пустая строка, короткое замыкание — OK")


if __name__ == "__main__":
    main()
