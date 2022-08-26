import sys

T = int(sys.stdin.readline())

for i in range(T):
    player1_sco = 0
    player2_sco = 0
    N = int(sys.stdin.readline())

    for i in range(N):
        P1, P2 = map(str, sys.stdin.readline().split())
        if(P1 == 'R'):
            if(P2 == 'S'):
                player1_sco += 1
            if(P2 == 'P'):
                player2_sco += 1
        if(P1 == 'S'):
            if(P2 == 'P'):
                player1_sco += 1
            if(P2 == 'R'):
                player2_sco += 1
        if(P1 == 'P'):
            if(P2 == 'R'):
                player1_sco += 1
            if(P2 == 'S'):
                player2_sco += 1

    if(player1_sco > player2_sco):
        print('Player 1')
    elif(player2_sco > player1_sco):
        print('Player 2')
    else:
        print('TIE')
