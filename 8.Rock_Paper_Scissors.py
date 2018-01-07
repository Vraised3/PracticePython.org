import random


def start():
    def RPS(A, B):
        if(A == 'Rock'):
            if(B == 'Scissors'):
                print('PlayerA wins')
            else:
                print('PlayerB wins')
        if(A == 'Paper'):
            if(B == 'Rock'):
                print('PlayerA wins')
            else:
                print('PlayerB wins')
        if(A == 'Scissors'):
            if(B == 'Rock'):
                print('Player A wins')
            else:
                print('Player B wins')
        Res = int(input('Do you want to restart(1) or exit(0): '))
        if(Res == 1):
            start()
        else:
            exit(0)

    def Matchup(PA, PB):
        print(PA, ' and ', PB)
        if(PA == PB):
            Res = int(input('Do you want to restart(1) or exit(0): '))
            if(Res == 1):
                start()
            else:
                exit(0)
        else:
            RPS(PA, PB)

    Options = ['Rock', 'Paper', 'Scissors']
    Game = int(input('1 Player or 2? '))
    PlayerA = input('PlayerA: Rock Paper or Scissors? ')
    if(PlayerA not in Options):
        print('Invalid input')
        start()
    if(Game == 1):
        PlayerB = random.choice(Options)
        Matchup(PlayerA, PlayerB)
    elif(Game == 2):
        PlayerB = input('PlayerB: Rock Paper or Scissors? ')
        Matchup(PlayerA, PlayerB)
    else:
        print('Invalid Number of players')
        Res = input('Do you want to restart(1) or exit(0): ')
        if(Res == 0):
            exit(0)


while(1):
    start()
