"""Пример 13. Встроенные функции на данных студентов."""

from __future__ import annotations


def main() -> None:
    """Проверить максимум, рейтинг, распаковку и кванторы."""
    print("Пример 13. Обработка данных студентов")
    students = [("Айгерим", 3.7), ("Бауыржан", 3.2), ("Виктор", 3.9)]
    best = max(students, key=lambda s: s[1])
    ranking = sorted(students, key=lambda s: s[1], reverse=True)
    print(best)
    print(ranking)
    names, gpas = zip(*students, strict=True)
    print(names, gpas)
    print(all(g >= 3.0 for g in gpas), any(g > 3.8 for g in gpas))
    for place, (name, gpa) in enumerate(sorted(students, key=lambda s: -s[1]), start=1):
        print(place, name, gpa)
    assert best == ("Виктор", 3.9)
    assert ranking == [("Виктор", 3.9), ("Айгерим", 3.7), ("Бауыржан", 3.2)]
    assert names == ("Айгерим", "Бауыржан", "Виктор") and gpas == (3.7, 3.2, 3.9)
    assert all(g >= 3.0 for g in gpas) and any(g > 3.8 for g in gpas)
    assert students[0] == ("Айгерим", 3.7)
    assert all([]) is True and any([]) is False
    print("Проверки: рейтинг, исходный порядок, zip, all и any — OK")


if __name__ == "__main__":
    main()
