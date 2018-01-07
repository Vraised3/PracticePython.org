def horizontal(size):
    print(' ---' * size, end='', flush=True)
    print('')


def vertical(size):
    print('|\t' * (size + 1), end='', flush=True)


def board_size(size):
    for x in range(0, size):
        horizontal(size)
        vertical(size)
        print('', end='\n', flush=True)
    horizontal(size)


xXx = int(input('How big should your board be? '))
board_size(xXx)
