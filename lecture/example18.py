"""Дополнительный пример 18. Все встроенные функции из таблицы лекции."""

from __future__ import annotations


def main() -> None:
    """Выполнить девять строк справочной таблицы встроенных функций."""
    print("Пример 18. Таблица встроенных функций")
    words = ["map", "filter", "zip"]
    xs = [-2, 1, -4, 3]
    keys, values = ["a", "b"], [10, 20]
    aggregate = (len(xs), sum(xs), min(xs), max(xs), max(words, key=len))
    ordered = sorted(xs, key=abs, reverse=True)
    backward = list(reversed(xs))
    quantifiers = (any(x < 0 for x in xs), all(x > 0 for x in xs))
    paired = dict(zip(keys, values, strict=True))
    numbered = list(enumerate(xs, 1))
    mapped = list(map(str, xs))
    filtered = list(filter(lambda x: x > 0, xs))
    progression = list(range(0, 10, 2))
    predicates = (isinstance(xs, list), callable(print), callable(xs))
    print("len/sum/min/max и max(key=len):", aggregate)
    print("sorted(key=abs, reverse=True):", ordered)
    print("reversed:", backward, "; any/all:", quantifiers)
    print("zip:", paired, "; enumerate:", numbered)
    print("map:", mapped, "; filter:", filtered)
    print("range:", progression, "; isinstance/callable:", predicates)
    assert aggregate == (4, -2, -4, 3, "filter")
    assert ordered == [-4, 3, -2, 1] and backward == [3, -4, 1, -2]
    assert quantifiers == (True, False) and paired == {"a": 10, "b": 20}
    assert numbered == [(1, -2), (2, 1), (3, -4), (4, 3)]
    assert mapped == ["-2", "1", "-4", "3"] and filtered == [1, 3]
    assert progression == [0, 2, 4, 6, 8] and predicates == (True, True, False)
    assert xs == [-2, 1, -4, 3]
    print("Проверки: все 9 строк таблицы, 15 встроенных функций — OK")


if __name__ == "__main__":
    main()
