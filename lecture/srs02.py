"""СРС 2. Немутирующее обновление вложенного словаря."""

from __future__ import annotations

from collections.abc import Hashable
from copy import deepcopy
from typing import Any


def _replace(
    d: dict[Hashable, Any], path: tuple[Hashable, ...], value: Any
) -> dict[Hashable, Any]:
    """Вернуть перестроенную ветвь, создавая отсутствующие словари."""
    head, *tail = path
    if not tail:
        return {**d, head: value}
    child = d.get(head, {})
    if not isinstance(child, dict):
        raise TypeError(f"Промежуточный ключ {head!r} содержит не словарь")
    return {**d, head: _replace(child, tuple(tail), value)}


def update_nested(
    d: dict[Hashable, Any], path: tuple[Hashable, ...], value: Any
) -> dict[Hashable, Any]:
    """Обновить непустой путь в независимой копии обычных данных Python.

    Отсутствующие ветви создаются. Несловарный промежуточный узел
    вызывает TypeError, пустой путь вызывает ValueError. Глубокое
    копирование изолирует вложенные изменяемые значения и value.
    """
    if not isinstance(d, dict):
        raise TypeError("d должен быть словарём")
    if not isinstance(path, tuple):
        raise TypeError("path должен быть кортежем ключей")
    if not path:
        raise ValueError("path не должен быть пустым")
    return _replace(deepcopy(d), path, deepcopy(value))


def main() -> None:
    """Проверить замену, создание ветвей, независимость и ошибки."""
    print("СРС 2. update_nested")
    original = {"student": {"name": "Алия", "scores": [80, 90]}, "active": True}
    snapshot = deepcopy(original)
    updated = update_nested(original, ("student", "name"), "Дана")
    print("Исходный:", original)
    print("Замена:", updated)
    assert updated["student"]["name"] == "Дана" and original == snapshot
    assert updated is not original and updated["student"] is not original["student"]
    created = update_nested(original, ("settings", "display", "theme"), "dark")
    print("Новая ветвь:", created["settings"])
    assert (
        created["settings"] == {"display": {"theme": "dark"}} and original == snapshot
    )
    value = [1, 2]
    isolated = update_nested(original, ("extra",), value)
    isolated["extra"].append(3)
    isolated["student"]["scores"].append(100)
    assert value == [1, 2] and original == snapshot
    assert update_nested({}, (1, "x"), 5) == {1: {"x": 5}}
    assert update_nested(original, ("active",), False)["active"] is False
    for path, error in [((), ValueError), (("active", "x"), TypeError)]:
        try:
            update_nested(original, path, 0)
        except error as exc:
            print(type(exc).__name__ + ":", exc)
        else:
            raise AssertionError("Ожидалась проверяемая ошибка")
    assert original == snapshot
    print("Проверки: замена, новые ветви, копии, пустой путь, конфликт — OK")


if __name__ == "__main__":
    main()
