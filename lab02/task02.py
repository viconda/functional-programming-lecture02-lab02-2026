"""Задание 2. Чистые немутирующие операции."""

import sys
from collections.abc import Callable, Hashable
from copy import deepcopy
from typing import Any, TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


def insert_at(lst: list[T], i: int, x: T) -> list[T]:
    """Вернуть список со вставкой по правилам list.insert."""
    index = min(i, len(lst)) if i >= 0 else max(0, len(lst) + i)
    return [*lst[:index], x, *lst[index:]]


def remove_all(lst: list[T], x: T) -> list[T]:
    """Вернуть новый список без всех значений, равных x."""
    return [item for item in lst if item != x]


def replace_where(
    lst: list[T],
    pred: Callable[[T], bool],
    value: T,
) -> list[T]:
    """Заменить подходящие элементы; pred должен быть чистым."""
    return [value if pred(item) else item for item in lst]


def rename_key(d: dict[K, V], old: K, new: K) -> dict[K, V]:
    """Переименовать ключ; отсутствие и коллизия вызывают ошибку."""
    if old not in d:
        raise KeyError(old)
    if new is not old and new != old and new in d:
        raise ValueError("Новый ключ уже существует")
    return {new if key is old or key == old else key: value for key, value in d.items()}


def update_in(
    d: dict[K, Any],
    path: tuple[K, ...],
    value: Any,
) -> dict[K, Any]:
    """Создать копии словарей вдоль непустого пути и установить value."""
    if not isinstance(path, tuple) or not path:
        raise ValueError("Путь должен быть непустым кортежем")
    key, *tail = path
    if not tail:
        return {**d, key: value}
    child = d.get(key, {})
    if not isinstance(child, dict):
        raise TypeError("Промежуточное значение не является словарём")
    return {**d, key: update_in(child, tuple(tail), value)}


def toggle(s: set[T], x: T) -> set[T]:
    """Вернуть множество с переключённым присутствием x."""
    return s ^ {x}


def is_even(value: int) -> bool:
    """Определить чётность целого числа."""
    return value % 2 == 0


def main(part: str) -> None:
    """Показать результат одной функции и неизменность её аргумента."""
    print(f"Задание 2: {part}")
    if part == "insert_at":
        source = [10, 20, 30]
        before = source[:]
        result = insert_at(source, -1, 99)
        assert result == [10, 20, 99, 30]
        print("Вход:", source, "индекс=-1, элемент=99")
    elif part == "remove_all":
        source = [1, 2, 1, 3, 1]
        before = source[:]
        result = remove_all(source, 1)
        assert result == [2, 3]
        print("Вход:", source, "удаляемое значение=1")
    elif part == "replace_where":
        source = [1, 2, 3, 4]
        before = source[:]
        result = replace_where(source, is_even, 0)
        assert result == [1, 0, 3, 0]
        print("Вход:", source, "чётные элементы заменить на 0")
    elif part == "rename_key":
        source = {"name": "Алия", "group": "CS-101"}
        before = source.copy()
        result = rename_key(source, "name", "student")
        assert result == {"student": "Алия", "group": "CS-101"}
        print("Вход:", source, "name -> student")
    elif part == "update_in":
        source = {"student": {"name": "Алия"}}
        before = deepcopy(source)
        result = update_in(source, ("student", "address", "city"), "Алматы")
        assert result["student"]["address"]["city"] == "Алматы"
        assert result["student"] is not source["student"]
        print("Вход:", source)
        print("Путь: ('student', 'address', 'city'), значение: Алматы")
    elif part == "toggle":
        source = {1, 2}
        before = source.copy()
        result = toggle(source, 2)
        added = toggle(source, 3)
        assert result == {1} and added == {1, 2, 3}
        print("Вход:", sorted(source), "переключаем 2 и отдельно 3")
        print("Результат добавления 3:", sorted(added))
    else:
        raise ValueError("Неизвестная функция")
    assert source == before and result is not source
    print("Результат:", sorted(result) if isinstance(result, set) else result)
    print("Аргумент после вызова:", source)
    print("Проверка: результат верен; исходный объект не изменён.")
    print("Проверка: возвращён новый объект.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "insert_at")
