"""Пример 12. Генераторные выражения."""

from __future__ import annotations


def main() -> None:
    """Проверить агрегирование генератора и раннее завершение any."""
    print("Пример 12. Генераторные выражения")
    total = sum(n * n for n in range(1_000_000))
    print(total)
    has_negative = any(x < 0 for x in [3, 5, -1, 7])
    print(has_negative)
    n = 999_999
    assert total == n * (n + 1) * (2 * n + 1) // 6
    assert total == 333332833333500000 and has_negative is True
    source = iter([3, 5, -1, 7])
    assert any(x < 0 for x in source) is True
    assert next(source) == 7
    g = (x * x for x in range(3))
    assert list(g) == [0, 1, 4] and list(g) == []
    assert sum(x for x in []) == 0 and any(x for x in []) is False
    print("any остановился на -1; число 7 осталось в исходном итераторе")
    print("Проверки: формула суммы, ранняя остановка, исчерпание — OK")


if __name__ == "__main__":
    main()
