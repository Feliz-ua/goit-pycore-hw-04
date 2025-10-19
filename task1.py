# Оголошуємо функцію total_salary, яка приймає як рядок один аргумент - шлях до текстового файлу   
def total_salary (path: str="salaries.txt"):
    # блок для перевірки можливих помилок. Якщо файл не знайдений - перехід до блоку except FileNotFoundError
    try:
        # Відкриваємо файл для читання з кодиванням UTF-8
        with open(path, "r",encoding="utf-8") as file:
            #Створюємо список для збереження зарплат усіх працівників
            salaries=[]
            #Створюємо цикл для проходження по кожному рядку файлу salaries.txt
            for line in file:
                # блок для перевірки можливих помилок. Якщо формат даних невірний - перехід до блоку except ValueError
                try:
                    # line.strip() - видаляємо пробіли, split(',') - розділяємо дані комою та просвоємо змінним "name" та "salary" значення з кожного рядка
                    name, salary = line.strip().split(',')
                    #Перетворюємо значення salary у ціле число 
                    salaries.append(int(salary))
                #except спрацює, якщо є помилка у форматі даних та неможливо виконати строку 14. Якщо є помилка - видає повідомлення про невірний формат даних
                except ValueError:
                    print(f"Невірний формат даних у рядку {line.strip()}")
        # Перевіряємо, чи список "salaries" порожній. Тобто якщо у файлі salaries.txt не має даних або формат даних невірний, 
        # то фнкція отримає значення 0,0 та завершить роботу 
        if not salaries:
            return 0, 0
        # Розрахуємо загальну суму заробітних плат
        total=sum(salaries)
        # Розрахуємо середне значення шляхом ділення загальної суми заробітних плат на кількість елементів
        average=total/len(salaries)
        # Поветаємо результат
        return total, average
    #except спрацює, якщо не знайден файл salaries.txt (рядки 4-6) та видає повідомлення про це
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
# Виклик функції та вивід результату
total,average=total_salary()
print(total)
print(average)
        
        
    
    
    
    
  