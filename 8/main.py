from validator import Validator, Data
from exceptions import ValidationError


def main():
    """Функция вызывает ввод имени и возраста. Введенные даные проверяются. В случае, если проверка не удалась, то
        выводится соответствующая ошибка и цикл начинается заново. Если проверка прошла успеешно, цикл останавливается.
        Функция выводит приветствие и рекомендации по замене паспорта, если соответствующая проверка прошла успешно.
        После приветствия запускается игра по угадыванию рандомного числа."""

    j = 0
    while True:

        j += 1
        print(f"{j}-ая попытка.")

        name = input("Введите ваше имя: ")
        age = input("Введите ваш возраст: ")

        data = Data(name, age)
        valid = Validator()

        try:
            valid.validate(data)
        except ValidationError as ex:
            print(f"Я поймал ошибку : {ex}")
            continue

        text = f"Привет, {name.title()}! Тебе {age} лет."
        print(text)
        break


if __name__ == '__main__':
    main()
