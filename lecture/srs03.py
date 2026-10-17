"""СРС 3. Частотный словарь букв русского текста."""

from __future__ import annotations


def letter_frequencies(text: str) -> dict[str, int]:
    """Посчитать русские буквы одним словарным включением.

    Регистр не учитывается, ё сохраняется отдельно от е.
    Пробелы, пунктуация, цифры и другие алфавиты исключаются.
    """
    normalized = text.lower()
    return {
        letter: normalized.count(letter)
        for letter in sorted(set(normalized))
        if letter in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    }


def main() -> None:
    """Сверить частоты с ручным подсчётом и проверить граничные входы."""
    print("СРС 3. Частотный словарь русских букв")
    text = "Мама мыла раму. Ёж и ёж!"
    actual = letter_frequencies(text)
    print("Текст:", text)
    print("Частоты:", actual)
    expected = {"а": 4, "ж": 2, "и": 1, "л": 1, "м": 4, "р": 1, "у": 1, "ы": 1, "ё": 2}
    assert actual == expected and sum(actual.values()) == 17
    assert letter_frequencies("") == {}
    assert letter_frequencies("  \t\n.,!? 123 ABC") == {}
    assert letter_frequencies("ЕеЁё") == {"е": 2, "ё": 2}
    assert letter_frequencies("Аа Бб") == {"а": 2, "б": 2}
    print("Всего русских букв:", sum(actual.values()))
    print("ЕеЁё:", letter_frequencies("ЕеЁё"))
    print("Проверки: ручной подсчёт, регистр, пробелы, ё и пустой вход — OK")


if __name__ == "__main__":
    main()
