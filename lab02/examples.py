"""Три демонстрационных примера из теории лабораторной работы."""

import sys
from typing import Any


def show(label: str, obj: object) -> None:
    """Вывести идентификатор и значение объекта как в методичке."""
    print(f"{label:<6} id={id(obj) % 10000:04d} value={obj}")


def aliases() -> None:
    """Выполнить пример присваивания и поверхностного копирования."""
    a = [1, 2]
    b = a
    c = a[:]
    b.append(3)
    show("a", a)
    show("b", b)
    show("c", c)
    print(a is b, a is c, a == c)
    assert a is b and a is not c and a != c
    assert a == [1, 2, 3] and c == [1, 2]


def handle(cmd: str) -> tuple[Any, ...]:
    """Разобрать учебную текстовую команду через match."""
    match cmd.split():
        case ["add", name, price]:
            return ("add", name, float(price))
        case ["del", name]:
            return ("del", name)
        case ["list"]:
            return ("list",)
        case ["find", *words] if words:
            return ("find", " ".join(words))
        case _:
            return ("error", cmd)


def commands() -> None:
    """Выполнить все шесть команд из демонстрационного примера."""
    source = ["add Ручка 150", "del Ручка", "list", "find синяя ручка", "find", "???"]
    result = [handle(command) for command in source]
    print("Вход:", source)
    print("\n".join(str(record) for record in result))
    assert result == [
        ("add", "Ручка", 150.0),
        ("del", "Ручка"),
        ("list",),
        ("find", "синяя ручка"),
        ("error", "find"),
        ("error", "???"),
    ]


def negative_revenue(item: tuple[str, int]) -> int:
    """Построить ключ убывания выручки."""
    return -item[1]


def sales_example() -> None:
    """Выполнить все пять запросов примера о продажах."""
    sales = (
        ("Алия", "ноутбук", "техника", 2, 380_000),
        ("Борис", "чайник", "быт", 5, 12_000),
        ("Алия", "мышь", "техника", 10, 6_000),
        ("Галым", "ноутбук", "техника", 1, 395_000),
        ("Борис", "пылесос", "быт", 2, 85_000),
    )
    managers = sorted({manager for manager, *_ in sales})
    revenue = {
        manager: sum(
            quantity * price for name, _, _, quantity, price in sales if name == manager
        )
        for manager in managers
    }
    best = max(revenue, key=revenue.__getitem__)
    categories = {category for _, _, category, _, _ in sales}
    all_positive = all(quantity > 0 and price > 0 for *_, quantity, price in sales)
    by_item = sorted(
        ((item, quantity * price) for _, item, _, quantity, price in sales),
        key=negative_revenue,
    )
    print("Выручка по менеджерам:", revenue)
    print("Лучший менеджер:", best)
    print("Категории:", sorted(categories), "| Все суммы положительны:", all_positive)
    print(
        "\n".join(
            f"{place}. {item:<8} {total:>9,}".replace(",", " ")
            for place, (item, total) in enumerate(by_item, start=1)
        )
    )
    assert revenue == {"Алия": 820000, "Борис": 230000, "Галым": 395000}
    assert best == "Алия" and categories == {"быт", "техника"} and all_positive
    assert by_item[-2:] == [("чайник", 60000), ("мышь", 60000)]


def main(part: str) -> None:
    """Выполнить выбранный пример из теоретической части."""
    print(f"Теоретический пример {part}")
    examples = {"1": aliases, "2": commands, "3": sales_example}
    examples[part]()
    print("Проверка: фактические результаты совпали с ожидаемыми.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1")
