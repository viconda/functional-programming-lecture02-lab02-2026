"""Проверки результатов и граничных случаев лабораторной работы."""

import contextlib
import io
import unittest
from copy import deepcopy
from math import isclose, pi

import examples
import task01
import task02
import task03
import task04
import task05


class ModelTests(unittest.TestCase):
    """Проверить все шесть фрагментов модели данных."""

    def test_fragments(self) -> None:
        """Сопоставить фактические значения и идентичность объектов."""
        with contextlib.redirect_stdout(io.StringIO()):
            matrix = task01.fragment_a()
            first, second = task01.fragment_b()
            nested = task01.fragment_c()
            strings = task01.fragment_d()
            changed, original = task01.fragment_e()
            consumed = task01.fragment_f()
        self.assertIs(matrix[0], matrix[2])
        self.assertIs(first, second)
        self.assertEqual(first, [1, 2, 3, 4])
        self.assertEqual(nested, (1, [2, 3, 4]))
        self.assertEqual(strings, ("abcd", "abc"))
        self.assertEqual((changed, original), ([1, 99], [1]))
        self.assertEqual(consumed, ([1, 2, 3], []))

    def test_examples(self) -> None:
        """Запустить проверки всех примеров из теоретической части."""
        with contextlib.redirect_stdout(io.StringIO()):
            examples.aliases()
            examples.commands()
            examples.sales_example()
        self.assertEqual(examples.handle("find одно два"), ("find", "одно два"))
        self.assertEqual(examples.handle("find"), ("error", "find"))


class PureOperationTests(unittest.TestCase):
    """Проверить чистоту и контракт шести операций."""

    def test_insert_matches_builtin(self) -> None:
        """Сверить крайние и отрицательные индексы с list.insert."""
        for source in ([], [1], [1, 2, 3]):
            for index in (-10, -3, -1, 0, 1, 3, 10):
                with self.subTest(source=source, index=index):
                    before = source[:]
                    expected = source[:]
                    expected.insert(index, 9)
                    result = task02.insert_at(source, index, 9)
                    self.assertEqual(result, expected)
                    self.assertEqual(source, before)
                    self.assertIsNot(result, source)

    def test_remove_all(self) -> None:
        """Проверить повторы, отсутствие значения и пустой список."""
        source = [1, 2, 1, 3, 1]
        self.assertEqual(task02.remove_all(source, 1), [2, 3])
        self.assertEqual(task02.remove_all(source, 7), source)
        self.assertIsNot(task02.remove_all(source, 7), source)
        self.assertEqual(task02.remove_all([], 1), [])
        self.assertEqual(source, [1, 2, 1, 3, 1])

    def test_replace_where(self) -> None:
        """Заменить подходящие элементы, сохранив исходный список."""
        source = [1, 2, 3, 4]
        self.assertEqual(task02.replace_where(source, task02.is_even, 0), [1, 0, 3, 0])
        self.assertEqual(task02.replace_where([], task02.is_even, 0), [])
        self.assertEqual(source, [1, 2, 3, 4])

    def test_rename_key(self) -> None:
        """Проверить порядок, отсутствие ключа и защиту от коллизии."""
        source = {"a": 1, "b": 2}
        result = task02.rename_key(source, "a", "c")
        self.assertEqual(list(result.items()), [("c", 1), ("b", 2)])
        self.assertEqual(task02.rename_key(source, "a", "a"), source)
        self.assertIsNot(task02.rename_key(source, "a", "a"), source)
        with self.assertRaises(KeyError):
            task02.rename_key(source, "missing", "x")
        with self.assertRaises(ValueError):
            task02.rename_key(source, "a", "b")
        self.assertEqual(source, {"a": 1, "b": 2})

    def test_update_in_copies_path(self) -> None:
        """Проверить копии по пути и неизменность вложенного аргумента."""
        source = {"student": {"name": "Алия"}, "meta": {"year": 2026}}
        before = deepcopy(source)
        result = task02.update_in(source, ("student", "city"), "Алматы")
        self.assertEqual(result["student"]["city"], "Алматы")
        self.assertEqual(source, before)
        self.assertIsNot(result, source)
        self.assertIsNot(result["student"], source["student"])
        self.assertIs(result["meta"], source["meta"])
        self.assertEqual(
            task02.update_in({}, ("a", "b", "c"), 7), {"a": {"b": {"c": 7}}}
        )
        self.assertEqual(task02.update_in({"a": 1}, ("a",), 2), {"a": 2})

    def test_rename_nan_identity(self) -> None:
        """Совпадение объекта ключа учитывается даже без равенства."""
        key = float("nan")
        source = {key: 7}
        self.assertEqual(task02.rename_key(source, key, "result"), {"result": 7})
        unchanged = task02.rename_key(source, key, key)
        self.assertEqual(unchanged[key], 7)
        self.assertIsNot(unchanged, source)
        self.assertEqual(source[key], 7)

    def test_update_in_bad_paths(self) -> None:
        """Не заменять молча скаляр словарём при ошибочном пути."""
        source = {"a": 1}
        with self.assertRaises(ValueError):
            task02.update_in(source, (), 7)
        with self.assertRaises(ValueError):
            task02.update_in(source, ["a"], 7)
        with self.assertRaises(TypeError):
            task02.update_in(source, ("a", "b"), 7)
        self.assertEqual(source, {"a": 1})

    def test_toggle(self) -> None:
        """Проверить обе ветви и обратимость переключения."""
        source = {1, 2}
        self.assertEqual(task02.toggle(source, 2), {1})
        self.assertEqual(task02.toggle(source, 3), {1, 2, 3})
        self.assertEqual(task02.toggle(task02.toggle(source, 2), 2), source)
        self.assertEqual(task02.toggle(set(), 3), {3})
        self.assertEqual(source, {1, 2})


class ComprehensionTests(unittest.TestCase):
    """Проверить десять решений включениями."""

    def test_squares(self) -> None:
        """Проверить число результатов и крайние значения."""
        result = task03.odd_squares()
        self.assertEqual((len(result), result[0], result[-1]), (15, 1, 841))

    def test_matrix(self) -> None:
        """Проверить таблицу, пустую и несимметричную матрицы."""
        table = task03.multiplication_table()
        self.assertEqual(table[4], [5, 10, 15, 20, 25])
        self.assertEqual(task03.transpose(table), table)
        self.assertEqual(
            task03.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]]
        )
        self.assertEqual(task03.transpose([]), [])
        self.assertIsNot(table[0], table[1])

    def test_flatten(self) -> None:
        """Проверить пустые вложенные списки и сохранность входа."""
        source = [[1, 2], [3], [], [4, 5, 6]]
        before = deepcopy(source)
        self.assertEqual(task03.flatten(source), [1, 2, 3, 4, 5, 6])
        self.assertEqual(task03.flatten([[], []]), [])
        self.assertEqual(source, before)

    def test_words(self) -> None:
        """Проверить границу длины и очистку краевой пунктуации."""
        self.assertEqual(task03.word_lengths("Мы дом, код! и я"), {"дом": 3, "код": 3})
        self.assertEqual(task03.word_lengths("я и ты"), {})

    def test_inversion(self) -> None:
        """Сохранить каждый ключ при повторяющихся значениях."""
        self.assertEqual(
            task03.invert_groups({"a": 1, "b": 2, "c": 1}), {1: ["a", "c"], 2: ["b"]}
        )
        self.assertEqual(task03.invert_groups({}), {})

    def test_vowels(self) -> None:
        """Проверить регистр, повторения, ё и отсутствие гласных."""
        self.assertEqual(task03.vowels("АаЕёIIO"), {"а", "е", "ё", "i", "o"})
        self.assertEqual(task03.vowels("123! бвг"), set())

    def test_triples(self) -> None:
        """Сверить полный набор троек с независимым перечнем."""
        expected = [
            (3, 4, 5),
            (5, 12, 13),
            (6, 8, 10),
            (7, 24, 25),
            (8, 15, 17),
            (9, 12, 15),
            (9, 40, 41),
            (10, 24, 26),
            (12, 16, 20),
            (12, 35, 37),
            (14, 48, 50),
            (15, 20, 25),
            (15, 36, 39),
            (16, 30, 34),
            (18, 24, 30),
            (20, 21, 29),
            (21, 28, 35),
            (24, 32, 40),
            (27, 36, 45),
            (30, 40, 50),
        ]
        self.assertEqual(task03.pythagorean_triples(), expected)

    def test_primes(self) -> None:
        """Сверить все простые числа и исключить единицу."""
        self.assertEqual(
            task03.primes(),
            [
                2,
                3,
                5,
                7,
                11,
                13,
                17,
                19,
                23,
                29,
                31,
                37,
                41,
                43,
                47,
                53,
                59,
                61,
                67,
                71,
                73,
                79,
                83,
                89,
                97,
            ],
        )

    def test_uppercase(self) -> None:
        """Проверить кириллицу, латиницу и отсутствие заглавных."""
        self.assertEqual(
            task03.uppercase_positions("АaБZ"), [(0, "А"), (2, "Б"), (3, "Z")]
        )
        self.assertEqual(task03.uppercase_positions("abc 123"), [])

    def test_digit_sum(self) -> None:
        """Сверить результат с независимым подсчётом разрядов."""
        self.assertEqual(task03.digit_sum(), 3 * 100 * sum(range(10)) + 1)


class StudentTests(unittest.TestCase):
    """Проверить все запросы к студентам и граничные случаи."""

    def test_queries_preserve_data(self) -> None:
        """Сопоставить результаты и исходные вложенные оценки."""
        source = task04.student_data()
        before = deepcopy(source)
        self.assertEqual(task04.best_student(source)[0], "Ганиева")
        self.assertEqual(task04.average(task04.best_student(source)), 95.0)
        self.assertTrue(task04.has_all_at_least_70(source))
        self.assertEqual(
            task04.group_counts(source), {"CS-101": 4, "CS-102": 4, "CS-103": 4}
        )
        names, averages = task04.parallel_columns(source)
        self.assertEqual(names[:2], ("Алиев", "Бекова"))
        self.assertEqual(averages[:2], (90.0, 80.0))
        self.assertEqual(task04.ranking(source)[0], (1, "Ганиева", 95.0))
        self.assertEqual(source, before)

    def test_stable_order(self) -> None:
        """Равный балл сохраняет порядок входных записей."""
        source = [("Б", "G", [90]), ("А", "G", [90]), ("В", "G", [100])]
        self.assertEqual([row[0] for row in task04.by_group(source)], ["В", "Б", "А"])
        self.assertEqual([row[1] for row in task04.ranking(source)], ["В", "Б", "А"])

    def test_empty_and_threshold(self) -> None:
        """Проверить границу 70, пустые списки и ошибку среднего."""
        self.assertTrue(task04.has_all_at_least_70([("А", "G", [70])]))
        self.assertFalse(task04.has_all_at_least_70([("А", "G", [69, 100])]))
        self.assertFalse(task04.has_all_at_least_70([("А", "G", [])]))
        self.assertFalse(task04.has_all_at_least_70([]))
        self.assertEqual(task04.parallel_columns([]), ((), ()))
        self.assertEqual(task04.ranking([]), [])
        with self.assertRaises(ValueError):
            task04.average(("А", "G", []))
        with self.assertRaises(ValueError):
            task04.best_student([])


class AreaTests(unittest.TestCase):
    """Проверить match, guards и суммарную площадь."""

    def test_valid_shapes(self) -> None:
        """Проверить четыре формулы и допустимый нулевой размер."""
        self.assertTrue(isclose(task05.area(("circle", 2)), 4 * pi))
        self.assertEqual(task05.area(("rect", 3, 4)), 12.0)
        self.assertEqual(task05.area(("square", 5)), 25.0)
        self.assertTrue(isclose(task05.area(("triangle", 3, 4, 5)), 6.0))
        self.assertEqual(task05.area(("circle", 0)), 0.0)
        self.assertEqual(task05.area(("rect", 0, 5)), 0.0)

    def test_invalid_shapes(self) -> None:
        """Проверить размеры, типы, форму кортежа и треугольник."""
        bad_shapes = [
            ("circle", -1),
            ("rect", 3, -4),
            ("square", -2),
            ("triangle", 1, 2, 3),
            ("triangle", 2, 1, 3),
            ("triangle", 3, 2, 1),
            ("triangle", 0, 1, 1),
            ("triangle", -3, 4, 5),
            ("circle", float("inf")),
            ("circle", float("nan")),
            ("square", True),
            ("rect", "3", 4),
            ("unknown", 2),
            ("circle",),
            ("square", 1, 2),
            ["circle", 2],
            None,
        ]
        for shape in bad_shapes:
            with self.subTest(shape=shape):
                self.assertIsNone(task05.area(shape))

    def test_total(self) -> None:
        """Суммировать только допустимые фигуры без изменения входа."""
        source = [
            ("circle", 2),
            ("rect", 3, 4),
            ("square", 5),
            ("triangle", 3, 4, 5),
            ("circle", -1),
        ]
        before = source[:]
        self.assertTrue(isclose(task05.total_area(source), 4 * pi + 43))
        self.assertEqual(task05.total_area([]), 0)
        self.assertEqual(task05.total_area([("bad",)]), 0)
        self.assertEqual(source, before)

    def test_large_dimensions(self) -> None:
        """Не допустить ложного переполнения Герона и необработанных ошибок."""
        expected = 3**0.5 / 4 * 1e200
        self.assertTrue(
            isclose(task05.area(("triangle", 1e100, 1e100, 1e100)), expected)
        )
        self.assertIsNone(task05.area(("circle", 10**400)))
        self.assertIsNone(task05.area(("square", 1e200)))
        self.assertIsNone(task05.area(("rect", 10**200, 10**200)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
