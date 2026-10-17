"""Измерить сумму квадратов чётных чисел от 2 до 10**7 включительно."""

import argparse
import gc
import json
import platform
import sys
import timeit
import tracemalloc
from collections.abc import Callable
from datetime import datetime, timezone
from functools import partial
from pathlib import Path
from statistics import median
from typing import Any

LIMIT = 10**7
REPEATS = 3
RESULTS_PATH = Path(__file__).with_name("benchmark_results.json")


def sum_loop(limit: int) -> int:
    """Сложить квадраты чётных чисел циклом с локальным аккумулятором."""
    total = 0
    for number in range(2, limit + 1, 2):
        total += number * number
    return total


def sum_list(limit: int) -> int:
    """Создать список квадратов чётных чисел и вычислить его сумму."""
    return sum([number * number for number in range(2, limit + 1, 2)])


def sum_generator(limit: int) -> int:
    """Вычислить сумму, последовательно получая квадраты из генератора."""
    return sum(number * number for number in range(2, limit + 1, 2))


def expected_sum(limit: int) -> int:
    """Получить точную сумму 4 * (1**2 + ... + m**2), где m = limit // 2."""
    m = max(0, limit // 2)
    return 4 * m * (m + 1) * (2 * m + 1) // 6


def measure_memory(function: Callable[[int], int], limit: int) -> dict[str, int]:
    """Замерить пик выделений Python отдельным вызовом без измерения времени."""
    gc.collect()
    tracemalloc.start()
    try:
        result = function(limit)
        current_bytes, peak_bytes = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return {
        "result": result,
        "current_bytes": current_bytes,
        "peak_bytes": peak_bytes,
    }


def run_benchmark() -> dict[str, Any]:
    """Выполнить три замера времени и отдельный замер памяти каждого способа."""
    methods = (
        ("loop", "Цикл с аккумулятором", sum_loop),
        ("list", "Списковое включение + sum", sum_list),
        ("generator", "Генераторное выражение + sum", sum_generator),
    )
    expected = expected_sum(LIMIT)
    # Это служебный измерительный код, а не функциональный запрос задания 6.
    rows = []
    for method_id, title, function in methods:
        # Небольшие проверки выполняются до измерений.
        assert all(function(n) == expected_sum(n) for n in (0, 1, 2, 9, 10))
        print(f"Измеряю время: {title}", flush=True)
        assert not tracemalloc.is_tracing()
        seconds = timeit.repeat(partial(function, LIMIT), number=1, repeat=REPEATS)
        print(f"Измеряю память отдельным вызовом: {title}", flush=True)
        memory = measure_memory(function, LIMIT)
        assert memory["result"] == expected
        rows.append(
            {
                "id": method_id,
                "title": title,
                "seconds": seconds,
                "median_seconds": median(seconds),
                "minimum_seconds": min(seconds),
                **memory,
            }
        )
    return {
        "measured_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "limit_inclusive": LIMIT,
        "number_of_even_values": LIMIT // 2,
        "timeit_number": 1,
        "timeit_repeat": REPEATS,
        "timing_has_tracemalloc": False,
        "expected_result": expected,
        "methods": rows,
    }


def display_results(results: dict[str, Any], saved: bool = False) -> None:
    """Показать измеренные значения, обозначив повторный просмотр файла."""
    print("Дополнительное задание. Сумма квадратов чётных чисел")
    if saved:
        print("Просмотр сохранённых фактических замеров. Новый замер не выполняется.")
    print(f"Дата замера UTC: {results['measured_at_utc']}")
    print(f"Python: {results['python'].splitlines()[0]}")
    print(f"Система: {results['platform']}")
    print("Диапазон: 2, 4, ..., 10 000 000 включительно. Элементов: 5 000 000.")
    print("timeit.repeat: number=1, repeat=3, tracemalloc выключен.")
    print("Память: отдельный запуск tracemalloc для каждого способа.")
    for row in results["methods"]:
        print(f"\n{row['title']}")
        print("Время, с: " + "; ".join(f"{value:.6f}" for value in row["seconds"]))
        print(f"Медиана: {row['median_seconds']:.6f} с")
        print(
            f"Пик памяти: {row['peak_bytes']} байт ({row['peak_bytes'] / 2**20:.3f} МиБ)"
        )
        print(f"Результат: {row['result']}")
    print(f"\nПо формуле 4*m*(m+1)*(2*m+1)//6: {results['expected_result']}")
    print("Все три результата совпадают с точной формулой.")


def main() -> None:
    """Выполнить измерение либо показать ранее сохранённый результат."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--show", action="store_true", help="показать сохранённый замер"
    )
    args = parser.parse_args()
    if args.show:
        results = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
        display_results(results, saved=True)
    else:
        results = run_benchmark()
        RESULTS_PATH.write_text(
            json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        display_results(results)


if __name__ == "__main__":
    main()
