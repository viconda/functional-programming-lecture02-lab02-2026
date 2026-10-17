"""Повторно выполнить практические задания и независимые проверки."""

import argparse
import ast
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    """Выполнить проверку с предсказуемой кодировкой вывода."""
    return subprocess.run(
        command,
        cwd=ROOT,
        env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )


def verify(group: str) -> None:
    """Запустить все отдельные демонстрации выбранной работы."""
    files = (
        (ROOT / "lecture/content.json",)
        if group == "lecture"
        else (ROOT / "lab02/content_main.json", ROOT / "lab02/content_extra.json")
    )
    sections = [
        section
        for file in files
        for section in json.loads(file.read_text(encoding="utf-8"))["sections"]
    ]
    print(f"Python {sys.version.split()[0]}. Проверка {group}")
    for section in sections:
        source = ROOT / section["code_file"]
        ast.parse(source.read_text(encoding="utf-8"), feature_version=(3, 10))
        run([sys.executable, str(source), *section.get("run_args", [])])
        print(section["id"] + ": PASS")
    print(f"Демонстрации и assert: {len(sections)} из {len(sections)} PASS")
    print("Синтаксис совместим с Python 3.10: PASS")
    if group == "lab":
        tests = run([sys.executable, "-m", "unittest", "discover", "-s", "lab02"])
        print((tests.stdout + tests.stderr).strip())
    print("Проверка завершена без ошибок.")


def main() -> None:
    """Выбрать лекцию, лабораторную или обе работы."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "group", choices=("lecture", "lab", "all"), default="all", nargs="?"
    )
    args = parser.parse_args()
    for group in ("lecture", "lab") if args.group == "all" else (args.group,):
        verify(group)


if __name__ == "__main__":
    main()
