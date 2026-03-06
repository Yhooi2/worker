"""
Основная программа для работы с классом WORKER.
Адаптирована под Университет «Синергия».
"""

from datetime import datetime
from worker import Worker


def main():
    workers = []  # список для хранения объектов Worker
    current_year = datetime.now().year

    # Ввод количества работников
    while True:
        try:
            n = int(input("Введите количество работников: "))
            if n <= 0:
                print("Ошибка: количество должно быть больше 0.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    # Ввод данных каждого работника
    for i in range(n):
        print(f"\n--- Работник {i + 1} ---")
        w = Worker()
        w.input_from_keyboard()
        workers.append(w)

    # Вывод всех работников
    print("\n=== Список всех работников ===")
    for i, w in enumerate(workers, 1):
        print(f"\nРаботник {i}:")
        w.display()

    # Запрос минимального стажа
    while True:
        try:
            min_exp = int(input("\nВведите минимальный стаж (лет): "))
            if min_exp < 0:
                print("Ошибка: стаж не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    # Фильтрация и вывод
    found = [w for w in workers if w.get_experience(current_year) > min_exp]

    if found:
        print(f"\nРаботники со стажем более {min_exp} лет:")
        for w in found:
            print(f"  - {w.get_name()} (стаж: {w.get_experience(current_year)} лет)")
    else:
        print(f"\nРаботники со стажем более {min_exp} лет не найдены.")


if __name__ == "__main__":
    main()
