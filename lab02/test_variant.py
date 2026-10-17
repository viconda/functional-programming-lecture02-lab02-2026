"""Проверки набора фильмов, границ запросов и неизменности аргументов."""

import unittest

from task06 import (
    FILMS,
    Film,
    Films,
    best_film_of_decade,
    directors_above_rating,
    films_longer_than,
)


class FilmQueryTests(unittest.TestCase):
    """Проверить результат каждого запроса и поведение на границах."""

    def test_dataset_shape(self) -> None:
        """Набор является кортежем как минимум из 12 пятиэлементных записей."""
        self.assertIsInstance(FILMS, tuple)
        self.assertGreaterEqual(len(FILMS), 12)
        self.assertTrue(
            all(isinstance(film, tuple) and len(film) == 5 for film in FILMS)
        )

    def test_duration_strict_boundary(self) -> None:
        """120 минут не удовлетворяет условию, 121 минута удовлетворяет."""
        short: Film = ("Короткий", "Автор", 2020, 119, 8.1)
        edge: Film = ("Граница", "Автор", 2020, 120, 8.1)
        long: Film = ("Длинный", "Автор", 2020, 121, 8.1)
        self.assertEqual(films_longer_than((short, edge, long)), (long,))

    def test_duration_dataset(self) -> None:
        """В полном наборе условию длительности соответствуют семь фильмов."""
        self.assertEqual(len(films_longer_than(FILMS)), 7)

    def test_decade_boundaries(self) -> None:
        """2010 и 2019 включаются, 2009 и 2020 исключаются."""
        before: Film = ("До", "Автор", 2009, 90, 10.0)
        start: Film = ("Начало", "Автор", 2010, 90, 8.0)
        end: Film = ("Конец", "Автор", 2019, 90, 9.0)
        after: Film = ("После", "Автор", 2020, 90, 10.0)
        self.assertEqual(best_film_of_decade((before, start, end, after), 2010), end)
        self.assertEqual(best_film_of_decade((before, start, after), 2010), start)

    def test_equal_ratings_keep_first(self) -> None:
        """max сохраняет первый максимум в исходном порядке."""
        first: Film = ("Первый", "Автор А", 2015, 90, 9.2)
        second: Film = ("Второй", "Автор Б", 2011, 90, 9.2)
        self.assertEqual(best_film_of_decade((first, second), 2010), first)
        self.assertEqual(best_film_of_decade((second, first), 2010), second)

    def test_empty_decade(self) -> None:
        """Отсутствие фильмов за десятилетие даёт None, а не исключение."""
        self.assertIsNone(best_film_of_decade(FILMS, 2030))

    def test_invalid_decade(self) -> None:
        """Некратное 10 или отрицательное начало считается ошибкой аргумента."""
        with self.assertRaises(ValueError):
            best_film_of_decade(FILMS, 2011)
        with self.assertRaises(ValueError):
            best_film_of_decade(FILMS, -10)

    def test_rating_strict_boundary_and_unique_names(self) -> None:
        """Учитывается оценка фильма > 8, имена не повторяются и сортируются."""
        films: Films = (
            ("A", "Борис", 2000, 90, 8.1),
            ("B", "Анна", 2001, 90, 9.0),
            ("C", "Борис", 2002, 90, 9.2),
            ("D", "Вера", 2003, 90, 8.0),
        )
        self.assertEqual(directors_above_rating(films), ("Анна", "Борис"))

    def test_any_qualifying_film_is_sufficient(self) -> None:
        """Наличие низкой оценки не отменяет другой фильм с оценкой > 8."""
        films: Films = (
            ("Удачный", "Автор", 2010, 90, 8.5),
            ("Неудачный", "Автор", 2011, 90, 3.0),
        )
        self.assertEqual(directors_above_rating(films), ("Автор",))

    def test_empty_dataset(self) -> None:
        """Все запросы определены и для пустого кортежа."""
        self.assertEqual(films_longer_than(()), ())
        self.assertIsNone(best_film_of_decade((), 2010))
        self.assertEqual(directors_above_rating(()), ())

    def test_input_unchanged(self) -> None:
        """Ни один из запросов не меняет переданный набор."""
        before = tuple(tuple(field for field in film) for film in FILMS)
        films_longer_than(FILMS)
        best_film_of_decade(FILMS, 2010)
        directors_above_rating(FILMS)
        self.assertEqual(FILMS, before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
