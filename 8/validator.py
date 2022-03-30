from exceptions import ValidationError


class Data:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()

    def _clear_whitespaces(self):
        """"Очищаем введенные данные от пробелов в начале и конце строки"""
        self.name = self.name.strip()
        self.age = self.age.strip()


class Validator:
    def __init__(self):
        """Конструктор, в котором создаем пустой список. Список будет принимать значения name и age."""
        self.data_history: list[Data] = []

    def validate(self, data: Data) -> None:
        """Метод, в котором список из конструктора класса Validator приобретает значения из класса Data.
        Далее вызываются методы валидации name,age."""

        self.data_history.append(data)
        self._validate_name()
        self._validate_age()

    def _validate_name(self) -> None:
        """Метод проверяет введенное пользователем имя. Из списка достает первый элемент соответствующий name.
         Проверяет на наличие введенного имени в списке; длину этого имени (не менее 3 символов);
         максимальное число пробелов в имени (не более 1 пробела).
         В случае, если условия не выполняются, возвращается определенная ошибка.
         Если ошибок нет, функция возвращает None."""

        name = self.data_history[0].name

        if not name:
            raise ValidationError("Вы не ввели имя.\n")

        elif len(name) < 3:
            raise ValidationError("Минимальная длина имени - 3 символа.\n")

        elif name.count(' ') > 1:
            raise ValidationError("Максимальное количество пробелов - 1 символ.\n")

    def _validate_age(self) -> None:
        """Метод проверяет введенный возраст пользователя. Из списка достает первый элемент соответствующий age (последний).
        Проверяет, чтобы возрост не был равен 0 или отрицательному числу;
        возраст был не менее 14 лет.
        В случае, если условия не выполняются, выводится определенная ошибка.
        Если ошибок нет, функция возвращает None."""

        age = int(self.data_history[-1].age)

        if age <= 0:
            raise ValidationError("Вам не может быть 0 лет или меньше.\n")

        elif age < 14:
            raise ValidationError("Программой запрещено пользоваться, если вам меньше 14 лет.\n")
