"""Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
  Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
   Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь."""
from random import randint as rnd

QUEEN = chr(9819)  # UNICODE queen


def check_up(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    for i in range(0, coord_row):
        # print(i)
        if board[i][coord_coll] == QUEEN:
            return False
    return True


def check_down(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    for i in range(coord_row + 1, 8):
        # print(i, coord_coll)
        if board[i][coord_coll] == QUEEN:
            return False
    return True


def check_right(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    for i in range(coord_coll + 1, 8):
        if board[coord_row][i] == QUEEN:
            return False
    return True


def check_left(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    for i in range(coord_coll - 1, 0, -1):
        if board[coord_row][i] == QUEEN:
            return False
    return True


def check_up_left(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    coord_row -= 1
    coord_coll -= 1
    while coord_coll >= 0 and coord_row >= 0:
        # print(coord_row, coord_coll)
        if board[coord_row][coord_coll] == QUEEN:
            return False
        coord_row -= 1
        coord_coll -= 1
    return True


def check_up_right(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    coord_row -= 1
    coord_coll += 1
    while coord_coll <= 7 and coord_row >= 0:
        # print(coord_row, coord_coll)
        if board[coord_row][coord_coll] == QUEEN:
            return False
        coord_row -= 1
        coord_coll += 1
    return True


def check_down_left(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    coord_row += 1
    coord_coll -= 1
    while coord_row <= 7 and coord_coll >= 0:
        # print(coord_row, coord_coll)
        if board[coord_row][coord_coll] == QUEEN:
            return False
        coord_row += 1
        coord_coll -= 1
    return True


def check_down_right(row: int, coll: int, board: list):
    coord_row = row
    coord_coll = coll
    coord_row += 1
    coord_coll += 1
    while coord_coll <= 7 and coord_row <= 7:
        # print(coord_row, coord_coll)
        if board[coord_row][coord_coll] == QUEEN:
            return False
        coord_row += 1
        coord_coll += 1
    return True


def check_all_possitions(*args):
    board = [['-'] * 8 for i in range(0, 8)]
    coords = list(map(lambda x: x - 1, args))
    for i in range(0, len(coords) - 1, 2):
        board[coords[i]][coords[i + 1]] = QUEEN
    # print(*board, sep='\n')
    # print(coords)
    check_lst = []
    for i in range(0, len(coords) - 1, 2):
        check_lst.append(check_up(coords[i], coords[i + 1], board))
        check_lst.append(check_down(coords[i], coords[i + 1], board))
        check_lst.append(check_right(coords[i], coords[i + 1], board))
        check_lst.append(check_left(coords[i], coords[i + 1], board))
        check_lst.append(check_up_right(coords[i], coords[i + 1], board))
        check_lst.append(check_down_right(coords[i], coords[i + 1], board))
        check_lst.append(check_up_left(coords[i], coords[i + 1], board))
        check_lst.append(check_down_left(coords[i], coords[i + 1], board))
        # print(coords[i], coords[i+1], check_lst)
        if not all(check_lst):
            return False
        check_lst.clear()
    return True


