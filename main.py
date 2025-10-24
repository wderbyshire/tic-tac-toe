
def collect_coords(board):
    valid_coord = False
    while not valid_coord:
        valid_coord = True
        # Collect and validate row choice
        valid_row = False
        while not valid_row:
            valid_row = True
            row_choice = input("Please select a row")

            if not row_choice.isnumeric():
                print("Please type the row as a number")
                valid_row = False
            else:
                row_choice = int(row_choice)

                if row_choice < 0 or row_choice > 2:
                    print("Please type a valid row between 0 and 2")
                    valid_row = False

        # Collect and validate column choice
        valid_col = False
        while not valid_col:
            valid_col = True
            col_choice = input("Please select a column")

            if not col_choice.isnumeric():
                print("Please type the column as a number")
                valid_col = False
            else:
                col_choice = int(col_choice)

                if col_choice < 0 or col_choice > 2:
                    print("Please type a valid column between 0 and 2")
                    valid_col = False

        # Check if chosen coordinates is empty
        if board[row_choice][col_choice] != "":
            print("That space is occupied, please select a different column")
            valid_coord = False

    return [row_choice, col_choice]

def player_turn(player_name, player_symbol, board):
    display_board(board)
    print("It's", player_name + "'s turn")

    chosen_coords = collect_coords(board)

    board[chosen_coords[0]][chosen_coords[1]] = player_symbol
    victory = check_for_victory(player_symbol, board)

    return victory

def check_for_victory(player_symbol, board):
    # Check horizontals
    for row in board:
        if row[0] == player_symbol and row[1] == player_symbol and row[2] == player_symbol:
            return True

    # Check horizontals
    for i in range(3):
        if board[0][i] == player_symbol and board[1][i] == player_symbol and board[2][i] == player_symbol:
            return True

    # Check left diagonal
    if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
        return True
    # Check right diagonal
    elif board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
        return True
    else:
        return False

def check_for_draw(board):
    total_pieces = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                total_pieces += 1

    if total_pieces == 9:
        return True
    else:
        return False

def display_board(board):
    for row in range(3):
        row_string = "| "
        for col in range(3):
            if board[row][col] == "":
                row_string += "- | "
            else:
                row_string += board[row][col] + " | "
        print(row_string)

def play_game():
    game_board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    p1_name = input("What is player 1's name?")
    p1_symbol = "X"

    p2_name = input("What is player's name?")
    p2_symbol = "O"

    current_player = p1_name
    current_symbol = p1_symbol
    game_over = False
    draw = False
    while not game_over and not draw:
        game_over = player_turn(current_player, current_symbol, game_board)
        draw = check_for_draw(game_board)

        if game_over:
            print()
            display_board(game_board)
            print(current_player, "wins!!")
        elif draw:
            print()
            display_board(game_board)
            print("It's a draw...")
        else:
            if current_player == p1_name:
                current_player = p2_name
                current_symbol = p2_symbol
            else:
                current_player = p1_name
                current_symbol = p1_symbol

        print()

play_game()