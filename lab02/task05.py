"""Задание 5. Площадь фигур с match и охранными условиями."""

import sys
from math import isclose, isfinite, pi, sqrt
from typing import TypeAlias

Shape: TypeAlias = tuple[object, ...]


def valid_size(value: object) -> bool:
    """Разрешить неотрицательные размеры, представимые конечным float."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return isfinite(value) and value >= 0
    except OverflowError:
        return False


def finite_area(value: float) -> float | None:
    """Вернуть площадь либо None, если результат не помещается в float."""
    return value if isfinite(value) else None


def area(shape: object) -> float | None:
    """Вычислить площадь допустимого кортежа или вернуть None."""
    if not isinstance(shape, tuple):
        return None
    match shape:
        case ("circle", r) if valid_size(r):
            return finite_area(pi * r * r)
        case ("rect", w, h) if valid_size(w) and valid_size(h):
            return finite_area(float(w) * float(h))
        case ("square", a) if valid_size(a):
            return finite_area(float(a) * float(a))
        case ("triangle", a, b, c) if (
            all(valid_size(side) for side in (a, b, c))
            and a + b > c
            and a + c > b
            and b + c > a
        ):
            # Нормирование предотвращает переполнение произведения Герона.
            scale = max(a, b, c)
            x, y, z = a / scale, b / scale, c / scale
            semiperimeter = (x + y + z) / 2
            factor = sqrt(
                max(
                    0.0,
                    semiperimeter
                    * (semiperimeter - x)
                    * (semiperimeter - y)
                    * (semiperimeter - z),
                )
            )
            return finite_area(factor * scale * scale)
        case _:
            return None


def total_area(shapes: list[Shape]) -> float:
    """Суммировать допустимые площади одним выражением."""
    return sum(value for shape in shapes if (value := area(shape)) is not None)


def main(part: str) -> None:
    """Показать корректные, граничные и ошибочные фигуры."""
    shapes = [
        ("circle", 2),
        ("rect", 3, 4),
        ("square", 5),
        ("triangle", 3, 4, 5),
        ("circle", 0),
        ("circle", -1),
        ("triangle", 1, 2, 3),
        ("unknown", 2),
        ("rect", "3", 4),
        ("square", True),
        ("circle", float("nan")),
    ]
    before = repr(shapes)
    print(f"Задание 5: {part}")
    if part == "area":
        print("\n".join(f"{shape!r} -> {area(shape)}" for shape in shapes))
        assert isclose(area(("circle", 2)), 4 * pi)
        assert area(("rect", 3, 4)) == 12.0
        assert area(("square", 5)) == 25.0
        assert isclose(area(("triangle", 3, 4, 5)), 6.0)
        assert area(("circle", 0)) == 0.0
        assert all(area(shape) is None for shape in shapes[5:])
    elif part == "sum":
        result = total_area(shapes)
        print("Вход: круг r=2; прямоугольник 3x4; квадрат 5; треугольник 3,4,5;")
        print("круг r=0 и 6 некорректных фигур из демонстрации area.")
        print("Площади допустимых фигур:", [area(shape) for shape in shapes[:5]])
        print("Суммарная площадь:", result)
        print("Ожидаемое значение: 4*pi + 12 + 25 + 6 =", 4 * pi + 43)
        assert isclose(result, 4 * pi + 43)
    else:
        raise ValueError("Допустимые режимы: area, sum")
    assert repr(shapes) == before
    print("Проверка: все assert выполнены; список фигур не изменён.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "area")
