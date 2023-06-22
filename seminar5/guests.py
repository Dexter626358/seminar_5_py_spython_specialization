# функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание
# Программа возвращает номер попытки с которой было угадана загадка или ноль, если попытки исчерпаны
# добавьте в модуль с загадками функцию, которая хранит словарь списков
# ключ словаря - загадка, а значение список с отгадками
# функция в цикле вызывает загадывающую функцию, чтобы передать ей список загадок


def puzzle(puzzle: str, answers: list, count_=3):
    try_ = 0
    print(f"Загадка - {puzzle}")
    while count_:
        user_answer = input("Ваш ответ: ").lower()

        if user_answer in answers:
            return try_

        try_ += 1
        count_ -= 1

    return 0


def list_puzzels():
    puzzles = {"Зимой и летом одним цветом?": ['ель', 'ёлка', 'елка'],
               "Висит груша - нельзя скушать": ['лампа', "лампочка"],
               "Не лает не кусает, а в дом не пускает": ["замок", "замочек"]}
    for key, value in puzzles.items():
       logger_(key, puzzle(key, value))

    print(_try_dict)


_try_dict = {}


def logger_(puzzle: str, num: int):
    global _try_dict
    _try_dict[puzzle] = num
