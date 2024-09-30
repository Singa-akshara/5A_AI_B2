import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print("Akshara Singa\n1BM22CS029")
def goal():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def printing():
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_full():
    for row in board:
        if ' ' in row:
            return False
    return True

def random_move():
    empty = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty.append((i, j))
    if empty:
        return random.choice(empty)
    return None

def find_best_move(player):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                if goal() == player:
                    return (i, j)
                board[i][j] = ' '
    return None

while True:
    printing()
    
    # User's turn
    row, col = map(int, input("Enter your move (row and column): ").split())
    if board[row][col] == ' ':
        board[row][col] = 'X'  # User's move
    else:
        print("Invalid move. Try again.")
        continue

    if goal() or is_full():
        break

    # AI's turn
    ai_move = find_best_move('O')  # Check for winning move
    if ai_move is None:
        ai_move = find_best_move('X')  # Check for blocking move
    if ai_move is None:
        ai_move = random_move()  # Make a random move
    
    if ai_move:
        board[ai_move[0]][ai_move[1]] = 'O'  # AI's move

    if goal() or is_full():
        break

# Final result
printing()
if goal() == 'X':
    print("You win!")
elif goal() == 'O':
    print("AI wins!")
else:
    print("It's a draw!")
