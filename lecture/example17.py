"""Дополнительный пример 17. Немутирующие альтернативы из таблицы лекции."""

from __future__ import annotations


def main() -> None:
    """Выполнить все шесть строк таблицы немутирующих операций."""
    print("Пример 17. Таблица немутирующих альтернатив")
    lst = [3, 1, 2]
    appended = [*lst, 4]
    ordered = sorted(lst)
    backward = list(reversed(lst))
    d = {"a": 1, "b": 2}
    updated = {**d, "a": 9}
    removed = {key: val for key, val in d.items() if key != "a"}
    s = {1, 2}
    extended = s | {3}
    print("append:", appended, "; sort:", ordered, "; reverse:", backward)
    print("Запись ключа:", updated, "; удаление ключа:", removed)
    print("add:", sorted(extended))
    assert appended == lst + [4] == [3, 1, 2, 4]
    assert ordered == [1, 2, 3] and backward == lst[::-1] == [2, 1, 3]
    assert updated == d | {"a": 9} == {"a": 9, "b": 2}
    assert removed == {"b": 2} and extended == {1, 2, 3}
    assert lst == [3, 1, 2] and d == {"a": 1, "b": 2} and s == {1, 2}
    print("Исходные list, dict, set сохранились:", lst, d, sorted(s))
    print("Проверки: все 6 строк таблицы и альтернативные записи — OK")


if __name__ == "__main__":
    main()
