def tictactoe():
    papan = [['#' for i in range(3)] for i in range(3)]

    def status():
        print('\nstatus papan')
        for i in range(3):
            for j in range(3):
                print(papan[i][j], end='')
            print()

    def menang():
        for i in range(3):
            if papan[i][0] == papan[i][1] == papan[i][2] and papan[i][0] != '#':
                return True
            if papan[0][i] == papan[1][i] == papan[2][i] and papan[0][i] != '#':
                return True
        if papan[1][1] != '#' and (papan[0][0] == papan[1][1] == papan[2][2] or papan[2][0] == papan[1][1] == papan[0][2]):
            return True
        return False

    def giliran(P):
        print('\nGiliran pemain', str(P))
        x = int(input('X: '))
        y = int(input('Y: '))

        while not (1 <= x <= 3 and 1 <= y <= 3):
            print('Kotak tidak valid')
            print('\nGiliran pemain', str(P))
            x = int(input('X: '))
            y = int(input('Y: '))
        
        while papan[x-1][y-1] != '#':
            print('Kotak sudah terisi. Silakan pilih kotak lain.')
            print('\nGiliran pemain', str(P))
            x = int(input('X: '))
            y = int(input('Y: '))

        papan[x-1][y-1] = str(P)

    print("Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2")
    status()

    for i in range(9):
        if i % 2: pemain = 'X'
        else: pemain = 'O'

        giliran(pemain)
        status()
        if menang():
            print("\nPemain", pemain, "menang.")
            break

        if i == 8:
            print('Seri.')