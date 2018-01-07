def horizontal(size):
    print(' ', end='')
    for x in range(0, size):
        print('---', end=' ', flush=True)
    print('')


def vertical(size):
    print('', end='', flush=True)
    for x in range(0, size + 1):
        print('|', end='\t', flush=True)


def board_size(size):
    for x in range(0, size):
        horizontal(size)
        vertical(size)
        print('', end='\n', flush=True)
    horizontal(size)


xXx = int(input('How big should your board be? '))
board_size(xXx)
