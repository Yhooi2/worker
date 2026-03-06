"""
Модуль worker.py
Описание класса WORKER для хранения данных о работниках
Университета «Синергия».
"""

from datetime import datetime


class Worker:
    """Класс, описывающий работника организации."""

    def __init__(self, name="", position="", salary=0.0, hire_year=0):
        """
        Конструктор с параметрами (по умолчанию — пустые значения).

        :param name: Фамилия и инициалы работника
        :param position: Название занимаемой должности
        :param salary: Заработная плата
        :param hire_year: Год поступления на работу
        """
        self._name = name
        self._position = position
        self._salary = salary
        self._hire_year = hire_year

    @classmethod
    def from_name_position(cls, name, position):
        """Конструктор с частичными параметрами (только ФИО и должность)."""
        return cls(name=name, position=position)

    def __del__(self):
        """Деструктор — выводит сообщение при удалении объекта."""
        pass  # в рабочей версии можно раскомментировать:
        # print(f"Объект работника {self._name} удален")

    # --- Геттеры ---
    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary

    def get_hire_year(self):
        return self._hire_year

    # --- Сеттеры с валидацией ---
    def set_name(self, name):
        if not name.strip():
            raise ValueError("ФИО не может быть пустым")
        self._name = name

    def set_position(self, position):
        if not position.strip():
            raise ValueError("Должность не может быть пустой")
        self._position = position

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary = salary

    def set_hire_year(self, hire_year):
        current_year = datetime.now().year
        if hire_year < 1900 or hire_year > current_year:
            raise ValueError(f"Год должен быть от 1900 до {current_year}")
        self._hire_year = hire_year

    # --- Методы ---
    def display(self):
        """Вывод всех полей объекта на экран."""
        print(f"  ФИО: {self._name}")
        print(f"  Должность: {self._position}")
        print(f"  Зарплата: {self._salary:.2f} руб.")
        print(f"  Год поступления: {self._hire_year}")

    def get_experience(self, current_year=None):
        """Вычисление стажа работы."""
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self._hire_year

    def input_from_keyboard(self):
        """Ввод данных работника с клавиатуры."""
        self._name = input("  Введите ФИО: ").strip()

        self._position = input("  Введите должность: ").strip()

        while True:
            try:
                self._salary = float(input("  Введите зарплату: "))
                if self._salary < 0:
                    print("  Ошибка: зарплата не может быть отрицательной.")
                    continue
                break
            except ValueError:
                print("  Ошибка: введите число.")

        current_year = datetime.now().year
        while True:
            try:
                self._hire_year = int(input("  Введите год поступления на работу: "))
                if self._hire_year < 1900 or self._hire_year > current_year:
                    print(f"  Ошибка: год должен быть от 1900 до {current_year}.")
                    continue
                break
            except ValueError:
                print("  Ошибка: введите целое число.")

    def __str__(self):
        return (f"{self._name} | {self._position} | "
                f"{self._salary:.2f} руб. | с {self._hire_year} г.")
