"""Пример 3. Изменяемый список внутри кортежа."""

from __future__ import annotations


def main() -> None:
    """Проверить поверхностную неизменяемость и хешируемость."""
    print("Пример 3. Список внутри кортежа")
    t = (1, [2, 3])
    before_id = id(t)
    t[1].append(4)
    print(t)
    assert id(t) == before_id and t == (1, [2, 3, 4])
    try:
        hash(t)
    except TypeError as exc:
        print("Ожидаемый TypeError:", exc)
    else:
        raise AssertionError("Кортеж со списком неожиданно хешируем")
    immutable = (1, (2, 3, 4))
    lookup = {immutable: "допустимый ключ"}
    assert lookup[(1, (2, 3, 4))] == "допустимый ключ"
    print("Кортеж с вложенным кортежем:", lookup[immutable])
    print("Проверки: вложенная мутация и ограничения hash — OK")


if __name__ == "__main__":
    main()
