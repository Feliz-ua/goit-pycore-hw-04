def parse_input(user_input):
    # Розбиваємо рядок введення на команду та аргументи
    cmd, *args = user_input.split()
    # Приводимо команду до нижнього регістру 
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
     # Перевірка чи передано два аргументи (ім'я і телефон)
    if len(args) < 2:
        return "Помилка: Будь ласка, вкажіть ім'я та телефон."
    # Розпаковуємо аргументи в змінні name і phone
    name, phone = args
    # Додаємо або оновлюємо контакт у словнику
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    # Перевіряємо наявність імені та нового номера телефону
    if len(args) < 2:
        return "Помилка: Будь ласка, вкажіть ім'я та новий номер телефону."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
     # Якщо ні — повертаємо повідомлення про помилку
    else:
        return "Помилка: Контакт не знайдено."

def show_phone(args, contacts):
    # Перевіряємо, чи вказане ім'я
    if len(args) < 1:
        return "Помилка: Будь ласка, вкажіть ім'я."
    name = args[0]
    # Повертаємо номер, якщо контакт знайдено
    if name in contacts:
        return contacts[name]
    else:
        return "Помилка: Контакт не знайдено."

def show_all(contacts):
    # Якщо словник порожній — повідомляємо про це
    if not contacts:
        return "Список контактів порожній."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    # Створюємо словник для контактів
    contacts = {}
    print("Welcome to the assistant bot!")
    # Створюємо нескінченний цикл прийому команд
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            # Якщо не має команди або невірна повідомляємо
            print("Невірна команда.")
            continue
        # Розбираємо введення на команду та аргументи
        command, args = parse_input(user_input)
        # Обробка команд
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Привітання
        elif command == "hello":
            print("How can I help you?")
        # Додавання контакту
        elif command == "add":
            print(add_contact(args, contacts))
        # Зміна номера контакту
        elif command == "change":
            print(change_contact(args, contacts))
       # Показ номера за ім'ям
        elif command == "phone":
            print(show_phone(args, contacts))
        # Показ всіх контактів
        elif command == "all":
            print(show_all(contacts))
        # Невірна команда
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
