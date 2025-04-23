def append_to_file(text, filename):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if (i + 1) % 2 == 0:
                    print(line, end='')
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования:
append_to_file("Первая строка", "example.txt")
append_to_file("Вторая строка", "example.txt")
append_to_file("Третья строка", "example.txt")
append_to_file("Четвертая строка", "example.txt")
append_to_file("Пятая строка", "example.txt")


