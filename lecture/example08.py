"""Пример 8. Протокол итерации."""

from __future__ import annotations


def main() -> None:
    """Получить значения вручную и проверить исчерпание итератора."""
    print("Пример 8. iter и next")
    nums = [10, 20, 30]
    it = iter(nums)
    first, second, third = next(it), next(it), next(it)
    print(first)
    print(second)
    print(third)
    ending = next(it, "конец")
    print(ending)
    assert [first, second, third] == nums and ending == "конец"
    assert iter(it) is it and list(it) == []
    try:
        next(it)
    except StopIteration:
        print("Повторный next без default: StopIteration")
    else:
        raise AssertionError("Исчерпанный итератор выдал значение")
    assert list(iter(nums)) == nums
    print("Новый итератор по тому же списку:", list(iter(nums)))
    print("Проверки: порядок, одноразовость, новый проход — OK")


if __name__ == "__main__":
    main()
