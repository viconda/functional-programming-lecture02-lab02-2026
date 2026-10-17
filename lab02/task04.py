"""Задание 4. Шесть запросов к данным двенадцати студентов."""

import sys
from copy import deepcopy
from typing import TypeAlias

Student: TypeAlias = tuple[str, str, list[int]]


def student_data() -> list[Student]:
    """Создать независимый набор из двенадцати студенческих записей."""
    return [
        ("Алиев", "CS-101", [90, 85, 95]),
        ("Бекова", "CS-102", [80, 75, 85]),
        ("Волков", "CS-101", [60, 70, 80]),
        ("Ганиева", "CS-103", [100, 95, 90]),
        ("Досов", "CS-102", [70, 70, 70]),
        ("Ермекова", "CS-101", [88, 92, 90]),
        ("Жуков", "CS-103", [50, 65, 80]),
        ("Зорина", "CS-102", [95, 90, 85]),
        ("Ибраев", "CS-101", [75, 80, 85]),
        ("Ким", "CS-103", [90, 90, 90]),
        ("Ли", "CS-102", [65, 70, 75]),
        ("Мусаева", "CS-103", [85, 80, 90]),
    ]


def average(student: Student) -> float:
    """Вычислить среднее; запись без оценок считать некорректной."""
    grades = student[2]
    if not grades:
        raise ValueError("У студента отсутствуют оценки")
    return sum(grades) / len(grades)


def best_student(students: list[Student]) -> Student:
    """Выбрать максимальный балл; при равенстве первую запись."""
    return max(students, key=average)


def group_order(student: Student) -> tuple[str, float]:
    """Создать ключ сортировки по группе и убыванию среднего."""
    return student[1], -average(student)


def by_group(students: list[Student]) -> list[Student]:
    """Стабильно отсортировать по группе и убыванию среднего."""
    return sorted(students, key=group_order)


def has_all_at_least_70(students: list[Student]) -> bool:
    """Проверить наличие студента с непустым набором оценок >= 70."""
    return any(
        bool(grades) and all(grade >= 70 for grade in grades)
        for _, _, grades in students
    )


def parallel_columns(
    students: list[Student],
) -> tuple[tuple[str, ...], tuple[float, ...]]:
    """Развернуть пары фамилия/средний балл в два кортежа."""
    return (
        tuple(zip(*((record[0], average(record)) for record in students), strict=True))
        if students
        else ((), ())
    )


def ranking(students: list[Student]) -> list[tuple[int, str, float]]:
    """Построить нумерованный с единицы стабильный рейтинг."""
    return [
        (place, student[0], average(student))
        for place, student in enumerate(
            sorted(students, key=average, reverse=True), start=1
        )
    ]


def group_counts(students: list[Student]) -> dict[str, int]:
    """Посчитать студентов каждой группы без изменения данных."""
    return {
        group: sum(student_group == group for _, student_group, _ in students)
        for group in sorted({group for _, group, _ in students})
    }


def main(part: str) -> None:
    """Запустить выбранный запрос и проверить сохранность данных."""
    students = student_data()
    before = deepcopy(students)
    print(f"Задание 4, запрос {part}; вход: {len(students)} студентов")
    print("Исходные записи (фамилия, группа, оценки):")
    print("\n".join(str(record) for record in students))
    if part == "1":
        result = best_student(students)
        print("Максимальный средний балл:", average(result))
        assert result[0] == "Ганиева" and average(result) == 95.0
    elif part == "2":
        result = [
            (record[0], record[1], average(record)) for record in by_group(students)
        ]
        assert [name for name, _, _ in result] == [
            "Алиев",
            "Ермекова",
            "Ибраев",
            "Волков",
            "Зорина",
            "Бекова",
            "Досов",
            "Ли",
            "Ганиева",
            "Ким",
            "Мусаева",
            "Жуков",
        ]
    elif part == "3":
        result = has_all_at_least_70(students)
        assert result is True
    elif part == "4":
        result = parallel_columns(students)
        assert len(result[0]) == len(result[1]) == 12
        assert tuple(zip(*result, strict=True)) == tuple(
            (student[0], average(student)) for student in students
        )
    elif part == "5":
        result = ranking(students)
        assert result[0] == (1, "Ганиева", 95.0)
        assert [
            name
            for _, name, _ in result
            if name in {"Алиев", "Ермекова", "Зорина", "Ким"}
        ] == ["Алиев", "Ермекова", "Зорина", "Ким"]
    elif part == "6":
        result = group_counts(students)
        assert result == {"CS-101": 4, "CS-102": 4, "CS-103": 4}
    else:
        raise ValueError("Запрос должен быть от 1 до 6")
    assert students == before
    print("Результат:", result)
    print("Проверка: результат верен; все исходные данные сохранены.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "1")
