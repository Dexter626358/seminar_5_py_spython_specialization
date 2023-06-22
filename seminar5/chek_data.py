"""Создайте модуль и напишите в нем функцию, которая проверяет формат даты
На вход функция получает дату в формате DD.MM.YYYY
Функция возвращает истину если дата верна и ложь, если нет
Для проверки висакосного года создайте отдельную функцию """


def _leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


def check_data(data: str):
    day, month, year = list(map(int, data.split(".")))
    if 1 < year < 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [2, 4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            return _leap_year(year) and day <= 29
    else:
        return False


if __name__ == "__name__":
    check_data("29.02.2023")
