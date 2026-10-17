"""Пример 1. Имена, ссылки, идентичность и равенство."""

from __future__ import annotations


def main() -> None:
    """Воспроизвести совмещение имён и проверить идентичность."""
    print("Пример 1. Имена и ссылки")
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
    print(a is b)
    print(id(a) == id(b))
    c = [1, 2, 3, 4]
    print(a == c, a is c)
    assert a == [1, 2, 3, 4] and a is b
    assert a == c and a is not c
    copied = a.copy()
    copied.append(5)
    assert a == [1, 2, 3, 4] and copied == [1, 2, 3, 4, 5]
    print("Проверки: общая ссылка, отдельный равный объект и копия — OK")


if __name__ == "__main__":
    main()
