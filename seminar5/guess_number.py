import random
import sys


def guess_num(tries=3, maximum=10, minimum=1):
    number = random.randint(minimum, maximum)

    while tries:
        answer = int(input("Введите число: "))
        if answer == number:
            print("Вы угадали!")
        else:
            if answer > number:
                print("Попробуйте взять меньше")
            else:
                print("Попробуйте взять больше")

        tries -= 1

    else:
        print("Вы не угадали")
        print("Загаданное число было ", number)



if __name__ == "__main__":
    guess_num(1, 10, 3)
