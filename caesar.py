# русский алфавит (33 буквы), отдельно строчные и заглавные,
# чтобы регистр букв сохранялся после сдвига
LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
UPPER = LOWER.upper()
SIZE = len(LOWER)


def shift_text(text, shift):
    # один проход по символам: буквы сдвигаем, всё остальное оставляем как есть
    result = ""
    for ch in text:
        if ch in LOWER:
            result += LOWER[(LOWER.index(ch) + shift) % SIZE]
        elif ch in UPPER:
            result += UPPER[(UPPER.index(ch) + shift) % SIZE]
        else:
            result += ch
    return result


def read_text():
    # пустая строка не имеет смысла, поэтому переспрашиваем
    while True:
        text = input("Введите строку: ")
        if text.strip():
            return text
        print("Ошибка: строка не должна быть пустой.")


def read_shift():
    # шаг ограничен размером алфавита, как требует задание
    while True:
        try:
            shift = int(input(f"Введите шаг сдвига (1-{SIZE}): "))
        except ValueError:
            print("Ошибка: шаг должен быть целым числом, например 5.")
            continue
        if 1 <= shift <= SIZE:
            return shift
        print(f"Ошибка: шаг должен быть от 1 до {SIZE}.")


def main():
    print("Шифр Цезаря")
    try:
        while True:
            print("\n1 - зашифровать")
            print("2 - расшифровать")
            print("0 - выход")
            choice = input("Выберите действие: ").strip()
            if choice == "0":
                break
            if choice not in ("1", "2"):
                print("Ошибка: введите 1, 2 или 0.")
                continue
            text = read_text()
            shift = read_shift()
            if choice == "1":
                print("Результат:", shift_text(text, shift))
            else:
                # расшифровка - это сдвиг в обратную сторону
                print("Результат:", shift_text(text, -shift))
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван. Выход.")


main()
