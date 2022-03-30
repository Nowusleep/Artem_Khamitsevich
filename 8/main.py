from validator import Validator, Data
from exceptions import ValidationError
from datetime import datetime


def get_passport_advice(age: int) -> str | None:
    """Рекомендации по действиям с паспортом. Если введенный пользователем возраст прошел проверки и функция проверки
    возраста не вернула ошибки,то возраст проверяется на три условия : значение меньше 17, но больше 16; значение
    меньше 26, но больше 25; значение меньше 46, но больше 45. В случае выполнения одного из условий возвращает
    соответствующие рекомендации. В противном случае функция возвращает None."""

    if 16 <= age <= 17:
        return "Не забудь получить первый паспорт по достижению 16 лет."

    elif 25 <= age <= 26:
        return "Не забудь заменить паспорт по достижению 25 лет."

    elif 45 <= age <= 46:
        return "Не забудь заменить паспорт по достижению 45 лет."


def main():
    """Функция вызывает ввод имени и возраста. Введенные даные проверяются. В случае, если проверка не удалась, то
        выводится соответствующая ошибка и цикл начинается заново. Если проверка прошла успеешно, цикл останавливается.
        Функция выводит приветствие и рекомендации по замене паспорта, если соответствующая проверка прошла успешно.
        После приветствия запускается игра по угадыванию рандомного числа."""

    j = 1

    start_time = datetime.now()

    while True:

        j += 1

        last_time = datetime.now()

        name = input("Введите ваше имя: ")
        age = input("Введите ваш возраст: ")

        data = Data(name, age)

        try:
            age = int(age)
        except ValueError:
            print("Возраст введен не корректно. Используйте числа.\n")
            print(f"{j}-ая попытка.")
            continue

        valid = Validator()

        try:
            valid.validate(data)
        except ValidationError as ex:
            print(f"Я поймал ошибку : {ex}")
            print(f"{j}-ая попытка.")
            continue

        advice = get_passport_advice(age)
        if advice is None:
            advice = ""

        text = f"Привет, {name.title()}! Тебе {age} лет. {advice}"
        print(text)
        break

    print(f"Вы ввели данные правильно с {j}-раза.")
    print(f"Время первой попытки : {start_time}")
    print(f"Время последней попытки : {last_time}")
    

if __name__ == '__main__':
    main()
