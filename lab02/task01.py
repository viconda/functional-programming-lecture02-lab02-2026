"""Задание 1. Исходные фрагменты и проверка предположений."""

import sys


def fragment_a() -> list[list[int]]:
    """Показать совместное использование одной строки матрицы."""
    x = [[0] * 3] * 3
    x[0][0] = 1
    print(x)
    assert x == [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    assert x[0] is x[1] is x[2]
    return x


def fragment_b() -> tuple[list[int], list[int]]:
    """Воспроизвести намеренную ошибку изменяемого default из условия."""

    # Учебный контрпример: [] намеренно оставлен как в условии.
    def add(item: int, bag: list[int] = []) -> list[int]:
        """Добавить элемент в общий объект параметра по умолчанию."""
        bag.append(item)
        return bag

    print(add(1), add(2))
    first, second = add(3), add(4)
    assert first is second and first == [1, 2, 3, 4]
    return first, second


def fragment_c() -> tuple[int, list[int]]:
    """Изменить список внутри неизменяемого кортежа."""
    t = (1, [2, 3])
    t[1].append(4)
    print(t)
    assert t == (1, [2, 3, 4])
    return t


def fragment_d() -> tuple[str, str]:
    """Показать перепривязку имени при конкатенации строк."""
    s = "abc"
    u = s
    s += "d"
    print(s, u, s is u)
    assert (s, u, s is u) == ("abcd", "abc", False)
    return s, u


def fragment_e() -> tuple[list[int], list[int]]:
    """Показать, что перепривязка параметра не меняет аргумент."""

    def change(lst: list[int]) -> list[int]:
        """Вернуть новый список с элементом 99."""
        lst = lst + [99]
        return lst

    data = [1]
    print(change(data), data)
    result = change(data)
    assert result == [1, 99] and data == [1] and result is not data
    return result, data


def fragment_f() -> tuple[list[int], list[int]]:
    """Исчерпать итератор и повторно попытаться прочитать его."""
    it = iter([1, 2, 3])
    print(list(it), list(it))
    another = iter([1, 2, 3])
    first, second = list(another), list(another)
    assert first == [1, 2, 3] and second == []
    return first, second


def main(part: str) -> None:
    """Запустить выбранный учебный фрагмент."""
    functions = {
        "a": fragment_a,
        "b": fragment_b,
        "c": fragment_c,
        "d": fragment_d,
        "e": fragment_e,
        "f": fragment_f,
    }
    predictions = {
        "a": "[[1, 0, 0], [1, 0, 0], [1, 0, 0]]",
        "b": "[1, 2] [1, 2]",
        "c": "(1, [2, 3, 4])",
        "d": "abcd abc False",
        "e": "[1, 99] [1]",
        "f": "[1, 2, 3] []",
    }
    letters = dict(zip("abcdef", "АБВГДЕ", strict=True))
    print(f"Задание 1, фрагмент {letters[part]}")
    print("Предполагаемый вывод:", predictions[part])
    print("Фактический вывод:")
    functions[part]()
    print("Проверка: предположение совпало; assert выполнены.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "a")
