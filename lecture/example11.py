"""Пример 11. Множественные и словарные включения."""

from __future__ import annotations


def main() -> None:
    """Проверить уникальность, словарь длин и обращение отображения."""
    print("Пример 11. Множества и словари")
    words = ["map", "filter", "reduce", "lambda", "map", "zip"]
    lengths = {len(w) for w in words}
    index = {w: len(w) for w in words}
    inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
    print(sorted(lengths))
    print(index)
    print(inverted)
    assert lengths == {3, 6}
    assert index == {"map": 3, "filter": 6, "reduce": 6, "lambda": 6, "zip": 3}
    assert inverted == {1: "a", 2: "b"}
    collision = {v: k for k, v in {"a": 1, "b": 1}.items()}
    assert collision == {1: "b"}
    print("Повтор значений при инверсии:", collision)
    print("Проверки: повтор слова, уникальные длины, коллизия ключа — OK")


if __name__ == "__main__":
    main()
