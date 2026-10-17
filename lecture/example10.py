"""Пример 10. Вложенные включения."""

from __future__ import annotations


def main() -> None:
    """Построить произведение, плоский список и транспонирование."""
    print("Пример 10. Вложенные включения")
    pairs = [(x, y) for x in "AB" for y in (1, 2, 3)]
    print(pairs)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [v for row in matrix for v in row]
    print(flat)
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(transposed)
    assert pairs == [("A", 1), ("A", 2), ("A", 3), ("B", 1), ("B", 2), ("B", 3)]
    assert flat == list(range(1, 10))
    assert transposed == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert [list(row) for row in zip(*transposed, strict=True)] == matrix
    assert matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [v for row in [[], [1, 2], []] for v in row] == [1, 2]
    print("Проверки: порядок, 6 пар, 9 элементов, обратное транспонирование — OK")


if __name__ == "__main__":
    main()
