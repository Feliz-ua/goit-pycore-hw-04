# імпортуємо модуль sys та класи і функції із модулей pathlib та colorama
import sys
from pathlib import Path
from colorama import init, Fore, Style
# Кольори: папки сині із /, файли — зелені, помилки — червоні

init(autoreset=True)

def print_directory_tree(path: Path, level=0):
     # Створюємо блок для обробки можливих помилок
    try:
        # Перевіряє, чи існує вказаний шлях
        if not path.exists():
            print(Fore.RED + f"Шлях не існує: {path}")
            return
        # Перебирає всі об'єкти у директорії, спочатку сортує їх.
        for item in sorted(path.iterdir()):
        # Формує відступ згідно з рівнем вкладеності.
            indent = ' ' * 4 * level
            if item.is_dir():
                # Якщо елемент — це папка, то виводить ім'я папки синім з / наприкінці
                print(f"{indent}{Fore.BLUE}{item.name}/" + Style.RESET_ALL)
                print_directory_tree(item, level + 1)
            else:
                # Якщо елемент — файл, виводить його зеленим.
                print(f"{indent}{Fore.GREEN}{item.name}" + Style.RESET_ALL)
    except Exception as e:
        # Винятки виводяться червоним кольором.
        print(Fore.RED + f"Помилка при обробці директорії: {e}")

def main():
    # Отримує шлях із аргументу, конвертує у об'єкт Path
    dir_path = Path(sys.argv[1])
    print_directory_tree(dir_path)
# Запуск main(), якщо скрипт — головна програма.
if __name__ == '__main__':
    main()