"""Показать сохранённый протокол фактической проверки Ruff."""

import json
from pathlib import Path


def main() -> None:
    """Прочитать протокол успешных запусков без повторного вызова Ruff."""
    path = Path(__file__).with_name("style_result.json")
    results = json.loads(path.read_text(encoding="utf-8"))
    print("Сохранённый протокол фактически выполненной проверки Ruff")
    print("Версия:", results["version"])
    print("Дата:", results["timestamp"])
    for check in results["checks"]:
        print("\nКоманда:", check["command"])
        print(check["output"].strip())
        print("Код завершения:", check["returncode"])
    print("\nPython 3.10+, группы правил E4, E7, E9, F, I, B, UP.")
    print("B006 разрешён только в task01.py: ошибка default дана в условии.")


if __name__ == "__main__":
    main()
