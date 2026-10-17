"""Задание 6, вариант 3: чистые запросы к учебному набору фильмов."""

import argparse

Film = tuple[str, str, int, int, float]
Films = tuple[Film, ...]

# Все названия, имена и оценки придуманы для учебного примера.
# Поля: название, режиссёр, год, длительность в минутах, оценка из 10.
FILMS: Films = (
    ("Письма в сентябре", "Елена Орлова", 1989, 118, 7.6),
    ("Город у моря", "Алексей Миронов", 1990, 121, 8.2),
    ("Долгая дорога", "Тимур Садыков", 1995, 142, 8.7),
    ("Последний трамвай", "Елена Орлова", 1999, 120, 8.0),
    ("Северный ветер", "Мария Белова", 2000, 125, 8.4),
    ("Линия горизонта", "Тимур Садыков", 2005, 137, 9.1),
    ("После дождя", "Алексей Миронов", 2009, 96, 8.9),
    ("Тихая станция", "Мария Белова", 2010, 123, 8.6),
    ("Точка возврата", "Данияр Ахметов", 2014, 155, 9.2),
    ("Свет в окне", "Наталья Волкова", 2019, 119, 9.2),
    ("День первый", "Данияр Ахметов", 2020, 120, 8.0),
    ("Открытое небо", "Ирина Соколова", 2024, 129, 7.9),
)


def films_longer_than(films: Films, minutes: int = 120) -> Films:
    """Вернуть фильмы строго длиннее minutes, сохранив порядок записей."""
    return tuple(film for film in films if film[3] > minutes)


def best_film_of_decade(films: Films, decade_start: int) -> Film | None:
    """Выбрать максимум оценки за годы [начало, начало + 10).

    Начало десятилетия должно быть кратно 10. При равенстве оценок
    возвращается первая запись в исходном кортеже, при отсутствии фильмов
    возвращается None.
    """
    if decade_start < 0 or decade_start % 10:
        raise ValueError("Начало десятилетия должно быть неотрицательным и кратным 10")
    return max(
        (film for film in films if decade_start <= film[2] < decade_start + 10),
        key=lambda film: film[4],
        default=None,
    )


def directors_above_rating(films: Films, threshold: float = 8.0) -> tuple[str, ...]:
    """Вернуть по алфавиту режиссёров хотя бы одного фильма с оценкой > порога."""
    return tuple(sorted({film[1] for film in films if film[4] > threshold}))


def format_film(film: Film) -> str:
    """Сформировать читаемую строку о фильме без выполнения вывода."""
    title, director, year, minutes, rating = film
    return f"{title}; {director}; {year}; {minutes} мин; {rating:.1f}"


def main() -> None:
    """Показать исходный набор или один из трёх независимых запросов."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", choices=("data", "1", "2", "3"))
    args = parser.parse_args()
    print("Лабораторная работа 2. Задание 6. Вариант 3")
    print("Учебные данные: все фильмы, имена и оценки вымышлены.")
    if args.query == "data":
        print(f"Исходный кортеж: {len(FILMS)} записей, по 5 полей.")
        print("Название; режиссёр; год; длительность; оценка")
        print("\n".join(format_film(film) for film in FILMS))
    elif args.query == "1":
        selected = films_longer_than(FILMS)
        print("Запрос 1. Фильмы длиннее 2 часов, строго > 120 минут:")
        print("\n".join(format_film(film) for film in selected))
        print(f"Найдено: {len(selected)}. Ровно 120 минут исключается.")
    elif args.query == "2":
        print("Запрос 2. Лучший фильм десятилетия 2010–2019:")
        best = best_film_of_decade(FILMS, 2010)
        print(format_film(best) if best is not None else "Нет фильмов")
        print("При оценке 9.2 у двух фильмов выбран первый в исходном кортеже.")
        print(f"Десятилетие 2030–2039 без записей: {best_film_of_decade(FILMS, 2030)}")
    else:
        print("Запрос 3. Режиссёры хотя бы одного фильма с оценкой строго > 8:")
        print("\n".join(directors_above_rating(FILMS)))
        print("Повторяющиеся имена удалены. Оценка ровно 8.0 исключается.")
    print(f"Исходный набор после запроса: {len(FILMS)} записей.")


if __name__ == "__main__":
    main()
