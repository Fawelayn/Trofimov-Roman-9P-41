board = [" "] * 9

All_win_lines = [[0,1,2], [3,4,5], [6,7,8],  # Строки
                 [0,3,6], [1,4,7], [2,5,8],  # Столбцы
                 [0,4,8], [2,4,6]  ] # Диагональ

def Build_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

Player = "X";
game_over = False
Count_move = 0

print("\nНачало игры!")

while not game_over and Count_move < 9:
    Build_board(board)
    print(f"\nИгрок {Player}, ваш ход.")

    try:
        move = int(input("Введите номер клетки (1-9): "))
    except:
        print("Ошибка! Нужно указать число от 1 до 9")
        continue
    
    if move < 1 or move > 9:
        print("Ошибка! Нужно указать число от 1 до 9")
        continue

    if board [move-1] != " ":
        print("Клетка занята! Выберите другую.")
        continue

    board[move-1] = Player
    Count_move += 1

    for line in All_win_lines:
        a, b, c, = line
        if board[a] == board[b] == board[c] != " ":
            Build_board(board)
            print(f"\nПобеда за игроком {Player} !")
            game_over = True
            break
    
    if Player == "X":
        Player = "O"
    else:
        Player = "X"

if not game_over:
    Build_board(board)
    print("\nНичья, все ячейки заполнены.")

print("Cпасибо за игру!")
