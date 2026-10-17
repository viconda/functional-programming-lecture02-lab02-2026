"""Пример 4. Call by sharing."""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def rebind(lst: list[int]) -> list[int]:
    """Перепривязать только локальное имя параметра."""
    lst = [0, 0, 0]
    return lst


def mutate(lst: list[int]) -> list[int]:
    """Добавить 99 в общий список для демонстрации побочного эффекта."""
    lst.append(99)
    return lst


def pure_append(lst: list[T], item: T) -> list[T]:
    """Вернуть новый список с добавленным элементом."""
    return [*lst, item]


def main() -> None:
    """Сравнить перепривязку, мутацию и создание новой коллекции."""
    print("Пример 4. Call by sharing")
    data = [1, 2, 3]
    rebound = rebind(data)
    print(data)
    assert data == [1, 2, 3] and rebound == [0, 0, 0]
    assert rebound is not data
    mutated = mutate(data)
    print(data)
    assert data == [1, 2, 3, 99] and mutated is data
    orig = [1, 2]
    new = pure_append(orig, 3)
    print(orig, new)
    assert orig == [1, 2] and new == [1, 2, 3] and new is not orig
    assert pure_append([], 7) == [7]
    print("Проверки: перепривязка, побочный эффект, чистое добавление — OK")


if __name__ == "__main__":
    main()
