board = list(range(1, 10))


def draw_board(brd):
    print("-" * 13)
    for i in range(3):
        print("|", brd[0 + i * 3], "|", brd[1 + i * 3], "|", brd[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
            if 1 <= player_answer <= 9:
                if str(board[player_answer - 1]) not in "XO":
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue


def check_win(brd):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if brd[each[0]] == brd[each[1]] == brd[each[2]]:
            return brd[each[0]]
    return False


def main(brd):
    counter = 0
    win = False
    while not win:
        draw_board(brd)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(brd)
            if tmp:
                print(tmp, "выиграл!")
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)


main(board)
