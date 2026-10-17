"""Пример 14. Распаковка последовательностей."""

from __future__ import annotations


def main() -> None:
    """Проверить звёздную распаковку и немутирующее объединение."""
    print("Пример 14. Распаковка")
    first, *middle, last = [1, 2, 3, 4, 5]
    print(first, middle, last)
    head, *tail = "функция"
    print(head, tail)
    a = [1, 2]
    b = [3, 4]
    merged = [*a, *b]
    cfg = {"debug": False, "level": 1}
    new_cfg = {**cfg, "debug": True}
    print(merged, cfg, new_cfg)
    assert (first, middle, last) == (1, [2, 3, 4], 5)
    assert head == "ф" and tail == list("ункция")
    assert merged == [1, 2, 3, 4] and a == [1, 2] and b == [3, 4]
    assert cfg == {"debug": False, "level": 1} and new_cfg == {
        "debug": True,
        "level": 1,
    }
    one, *rest = [7]
    assert one == 7 and rest == []
    print("Проверки: крайние элементы, строка, объединение, пустой хвост — OK")


if __name__ == "__main__":
    main()
