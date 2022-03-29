from exceptions import ValidationError
from datetime import datetime


class Data:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()
        self.age = int(self.age)

    def _clear_whitespaces(self):
        """"Очищаем введенные данные от пробелов в начале и конце строки"""
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    def __init__(self):
        Data.__init__(self, self.name, self.age)
        current_time = datetime.utcnow().time()
        print(current_time)


class Validator:
    def __init__(self):
        """Конструктор, в котором создаем пустой список. Список будет принимать значения name и age."""
        self.data_history = []

    def validate(self, data: Data) -> None:
        """Метод, в котором список приобретает значения из класса Data"""
        self.data_history.append(data)
        self._validate_list()
        self._validate_name()
        self._validate_age()

    def _validate_list(self):
        if not self.data_history:
            raise ValueError("Вы не ввели никаких данных. Попробуйте еще раз")

    def _validate_name(self) -> None:

        name = self.data_history[0].name
        if not name:
            raise ValidationError("Вы не ввели имя.\n")

        elif len(name) < 3:
            raise ValidationError("Минимальная длина имени - 3 символа.\n")

        elif name.count(' ') > 1:
            raise ValidationError("Максимальное количество пробелов - 1 символ.\n")

    def _validate_age(self) -> None:

        age = self.data_history[-1].age

        if not age:
            raise ValidationError("Вы не ввели возраст")

        if age <= 0:
            raise ValidationError("Вам не может быть 0 лет или меньше.\n")

        elif age < 14:
            raise ValidationError("Программой запрещено пользоваться, если вам меньше 14 лет.\n")
