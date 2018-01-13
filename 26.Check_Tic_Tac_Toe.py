def same(same3):  # Check if the elements are the same
    if(0 in same3):
        return 0
    if(same3[0] == same3[1] and same3[1] == same3[2]):
        return 1
    else:
        return 0


def win(board):  # See who wins, Diagonal, Row & Column
    same3 = []
    '''Diagonal'''
    for i in range(0, 3):
        same3.append(board[i][i])
    if(same(same3) == 1):
        for i in range(0, 3):
            board[i][i] = '-'
        return [1, board]
    same3 = []

    for i in range(0, 3):
        same3.append(board[i][2 - i])
    if(same(same3) == 1):
        for i in range(0, 3):
            board[i][2 - i] = '-'
        return [1, board]
    same3 = []

    '''Horizontal'''
    for i in range(0, 3):
        same3 = board[i][:]
        if(same(same3) == 1):
            board[i][:] = ['-', '-', '-']
            return [1, board]
    same3 = []

    '''Vertical'''
    for i in range(0, 3):
        same3 = [row[i] for row in board]
        if(same(same3) == 1):
            board = [list(x) for x in zip(*board)]
            print(board)
            board[i][:] = ['-', '-', '-']
            return [1, list(zip(*board))]
    same3 = []

    return [0, board]


def write(board, Player):
    [x, y] = [int(input()) for a in range(0, 2)]
    board[x][y] = Player
    return board


def game(board):  # Main Game Event
    P1 = 'x'
    P2 = 'O'

    while(1):
        print('Player P1 which index[i][j] do you choose? ')
        [w, board] = win(write(board, P1))
        for i in board:
            print(*i)
        if(w == 1):
            print('Player P1 wins')
            exit(0)

        print('Player P2 which index[i][j] do you choose? ')
        [w, board] = win(write(board, P2))
        for i in board:
            print(*i)
        if(w == 1):
            print('Player P2 wins')
            exit(0)


board = [[0 for a in range(3)] for b in range(3)]  # Blank Board created
game(board)
