"""Пример 15. Аннотации и функции высшего порядка."""

from __future__ import annotations

import math
from collections.abc import Callable, Iterable


def apply_all(funcs: Iterable[Callable[[float], float]], x: float) -> list[float]:
    """Применить каждую функцию к x и вернуть список результатов."""
    return [f(x) for f in funcs]


def main() -> None:
    """Проверить список и генератор функций, а также пустой вход."""
    print("Пример 15. Callable и Iterable")
    actual = apply_all([math.sqrt, math.log10, abs], 100.0)
    print(actual)
    assert actual == [10.0, 2.0, 100.0]
    funcs = (f for f in (abs, math.sqrt))
    assert apply_all(funcs, 9.0) == [9.0, 3.0]
    assert apply_all([], 100.0) == []
    assert apply_all([abs], -5.0) == [5.0]
    print("Проверки: список функций, генератор, пустой вход и abs — OK")


if __name__ == "__main__":
    main()
