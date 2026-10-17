"""СРС 1. Десять изменяющих методов и немутирующие аналоги."""

from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
from typing import Any


def compare(
    name: str, original: Any, mutate: Callable[[Any], Any], pure: Callable[[Any], Any]
) -> None:
    """Сравнить новое значение с результатом мутации отдельной копии."""
    snapshot = deepcopy(original)
    target = deepcopy(original)
    mutate(target)
    actual = pure(original)
    assert actual == target, name
    assert original == snapshot, name
    assert actual is not original, name
    shown = sorted(actual) if isinstance(actual, set) else actual
    print(name + ":", shown, "| исходный объект сохранён")


def main() -> None:
    """Проверить ровно десять методов, дубликаты и ошибку remove."""
    print("СРС 1. 10 методов и немутирующие выражения")
    compare("list.append", [1, 2], lambda a: a.append(3), lambda a: [*a, 3])
    compare("list.extend", [1], lambda a: a.extend([2, 3]), lambda a: [*a, *[2, 3]])
    compare(
        "list.remove",
        [2, 1, 2],
        lambda a: a.remove(2),
        lambda a: (lambda i: a[:i] + a[i + 1 :])(a.index(2)),
    )
    compare("list.reverse", [3, 1, 2], lambda a: a.reverse(), lambda a: a[::-1])
    compare("list.sort", [3, 1, 2], lambda a: a.sort(), lambda a: sorted(a))
    compare("list.clear", [1, 2], lambda a: a.clear(), lambda a: [])
    compare(
        "dict.update",
        {"a": 1, "b": 2},
        lambda d: d.update({"b": 9, "c": 3}),
        lambda d: {**d, **{"b": 9, "c": 3}},
    )
    compare("dict.clear", {"a": 1}, lambda d: d.clear(), lambda d: {})
    compare("set.add", {1, 2}, lambda s: s.add(3), lambda s: s | {3})
    compare("set.discard", {1, 2}, lambda s: s.discard(2), lambda s: s - {2})
    original = [1, 2, 1]
    actual = (lambda i: original[:i] + original[i + 1 :])(original.index(1))
    assert actual == [2, 1] and original == [1, 2, 1]
    assert {1, 2} - {99} == {1, 2}
    try:
        (lambda i: original[:i] + original[i + 1 :])(original.index(99))
    except ValueError:
        print("remove отсутствующего элемента: ожидаемый ValueError")
    else:
        raise AssertionError("Ожидался ValueError")
    print("Проверки: 10 пар, первое вхождение, отсутствующие элементы — OK")


if __name__ == "__main__":
    main()
