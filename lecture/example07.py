"""Пример 7. Сопоставление с образцом."""

from __future__ import annotations

from typing import Any


def describe(shape: Any) -> str:
    """Описать кортеж фигуры; размеры в примере являются числами."""
    match shape:
        case ("circle", r):
            return f"круг, площадь {3.14159 * r * r:.2f}"
        case ("rect", w, h) if w == h:
            return f"квадрат со стороной {w}"
        case ("rect", w, h):
            return f"прямоугольник {w}x{h}"
        case _:
            return "неизвестная фигура"


def main() -> None:
    """Проверить каждую ветвь match, включая защитное условие."""
    print("Пример 7. match/case")
    shapes = [("circle", 1), ("rect", 2, 2), ("rect", 2, 5), ("triangle",)]
    actual = [describe(s) for s in shapes]
    for description in actual:
        print(description)
    assert actual == [
        "круг, площадь 3.14",
        "квадрат со стороной 2",
        "прямоугольник 2x5",
        "неизвестная фигура",
    ]
    assert describe(("circle", 0)) == "круг, площадь 0.00"
    assert describe(("rect", 2)) == "неизвестная фигура"
    print("Проверки: четыре ветви, нулевой радиус, неверная длина — OK")


if __name__ == "__main__":
    main()
