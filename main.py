from seminar5 import check_data, guess_number, chek_data
from seminar5 import check_all_possitions
from random import randint as rnd
import sys

""" В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""
#init_data = list(map(str, [i for i in sys.argv][1:]))
#print(chek_data.check_data(*init_data))


"""Добавьте в пакет, созданный на семинаре шахматный модуль.
 Внутри него напишите код, решающий задачу о 8 ферзях.
  Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. """


found_true_possition = {}
count_ = 1
for i in range(1, 500_000):
    possition_lst = []
    for j in range(1, 17):
        possition_lst.append(rnd(1, 8))
    if check_all_possitions(*possition_lst):
        found_true_possition[count_] = possition_lst
        count_ += 1

for key, value in found_true_possition.items():
    print(f"{key} : {value}, {check_all_possitions(*value)}")


#print(check_all_possitions(1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8))

