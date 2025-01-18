from environs import Env

TRANSLIT_RULES = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "YO",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "Y",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TS",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ъ": "",
    "Ы": "Y",
    "Ь": "",
    "Э": "E",
    "Ю": "YU",
    "Я": "YA",
}


def transliterate(name):
    """Транслитерирует русское имя или фамилию на латиницу."""
    normalized_name = name.upper()
    return "".join(TRANSLIT_RULES.get(char, char) for char in normalized_name)


if __name__ == "__main__":
    env = Env()
    env.read_env()

    # Чтение переменной для входного и выходного файла из .env
    default_input_file = env.str("INPUT_FILE", "names.txt")
    default_output_file = env.str("OUTPUT_FILE", "transliterated_names.txt")

    # Запрос пути к входному файлу
    print(
        "Введите путь к входному файлу (нажмите Enter для использования пути из .env):"
    )
    input_file = input().strip() or default_input_file

    # Запрос имени выходного файла
    print("Введите имя выходного файла (нажмите Enter для использования пути из .env):")
    output_file = input().strip() or default_output_file

    try:
        with (
            open(input_file, "r", encoding="utf-8") as infile,
            open(output_file, "w", encoding="utf-8") as outfile,
        ):
            for line in infile:
                russian_name = line.strip()
                if russian_name:  # Проверяем, что строка не пустая
                    latin_name = transliterate(russian_name)
                    outfile.write(f"{latin_name}\n")
        print(f"Транслитерация завершена. Результаты сохранены в {output_file}.")
    except FileNotFoundError:
        print(f"Файл {input_file} не найден. Убедитесь, что путь указан верно.")
