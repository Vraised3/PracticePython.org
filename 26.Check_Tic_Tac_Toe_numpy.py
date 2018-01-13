import numpy as np

board = np.zeros([3, 3])
players = {'P1': 1, 'P2': 2}
print(board)


def win(board):
    for Player in players:
        # Diagonal Check
        if(np.array_equal(board.diagonal(), [players[Player] for a in range(3)])):
            print(Player + ' wins')
            board[np.diag_indices(3)] = 10
            print(board)
            exit(0)
        elif(np.array_equal(np.fliplr(board).diagonal(), [players[Player] for a in range(3)])):
            np.fliplr(board)[np.diag_indices(3)] = 10
            print(Player + ' wins')
            print(board)
            exit(0)

        for i in range(3):
            # Horizontal Check
            if(np.array_equal(board[i, :], [players[Player] for a in range(3)])):
                board[i, :] = 10
                print(Player + ' wins')
                print(board)
                exit(0)
            # Vertical Check
            if(np.array_equal(board[:, i], [players[Player] for a in range(3)])):
                board[:, i] = 10
                print(Player + ' wins')
                print(board)
                exit(0)
        return


def write(board, ind, P):
    board[ind[0], ind[1]] = P
    return board


def play():
    while(1):
        print('Player 1 please enter your index: ')
        P1Ind = [int(input()) for a in range(0, 2)]
        win(write(board, P1Ind, players['P1']))
        print(board)
        print('Player 2 please enter your index: ')
        P2Ind = [int(input()) for a in range(0, 2)]
        win(write(board, P2Ind, players['P2']))
        print(board)


play()
