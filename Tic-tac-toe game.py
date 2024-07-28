import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('|'.join(row))
        print('-' * 5)

def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    for condition in win_conditions:
        if condition.count(player) == 3:
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = 'O'

def player_move(board, move):
    if board[move] == ' ':
        board[move] = 'X'
        return True
    return False

def play_game():
    print_board(board)
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if player_move(board, move):
            print_board(board)
            if is_winner(board, 'X'):
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
            ai_move(board)
            print_board(board)
            if is_winner(board, 'O'):
                print("AI wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break
        else:
            print("Invalid move. Try again.")

play_game()