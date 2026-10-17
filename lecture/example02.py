"""Пример 2. Неизменяемые значения."""

from __future__ import annotations


def main() -> None:
    """Проверить строку, число и запрет присваивания в кортеж."""
    print("Пример 2. Неизменяемые значения")
    s = "функция"
    t = s.upper()
    print(s, t)
    x = 10
    print(id(x) == id(x + 1))
    point = (3, 4)
    moved = (point[0] + 1, point[1])
    print(point, moved)
    assert s == "функция" and t == "ФУНКЦИЯ"
    assert x == 10 and point == (3, 4) and moved == (4, 4)
    try:
        point[0] = 5  # type: ignore[index]
    except TypeError as exc:
        print("Ожидаемый TypeError:", exc)
    else:
        raise AssertionError("Кортеж разрешил замену элемента")
    print("Проверки: исходные значения сохранены, TypeError получен — OK")


if __name__ == "__main__":
    main()
