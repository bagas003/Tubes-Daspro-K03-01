# B03 - Tic Tac Toe
def tictactoe():
    # Platform bermain tic tac toe untuk pengguna
    # I.S. menerima masukan dari 2 pengguna berbeda untuk setiap giliran
    # F.S. menampilkan status kemenangan pemain

    # KAMUS
    # procedure status(output: string)
    # function menang() -> bool
    # procedure giliran(input: P, x, y)
    # papan : array of array of char
    # i, j, x, y : integer
    # P, pemain : character

    # Inisialisasi
    papan = [[' ' for i in range(3)] for i in range(3)]
    
    # Realisasi Prosedur dan Fungsi
    def status():
        # menampilkan keadaan papan saat ini ke layar
        print('\nstatus papan:')
        print('  x 1   2   3\ny +---+---+---+')
        for i in range(3):
            print(i+1, '| ', end='')
            for j in range(3):
                print(papan[i][j], end=' | ')
            print('\n  +---+---+---+')

    def menang():
        # mengembalikan nilai True jika sudah ada yang menang, dan sebaliknya
        for i in range(3):
            if papan[i][0] == papan[i][1] == papan[i][2] and papan[i][0] != ' ':
                return True, "horizontal"
            if papan[0][i] == papan[1][i] == papan[2][i] and papan[0][i] != ' ':
                return True, "vertikal"
        if papan[1][1] != ' ' and (papan[0][0] == papan[1][1] == papan[2][2] or papan[2][0] == papan[1][1] == papan[0][2]):
            return True, "diagonal"
        return False

    def giliran(P):
        # Sebagai input pemain setiap giliran
        # input harus divalidasi terlebih dahulu
        print('\nGiliran pemain', str(P))
        x = int(input('kolom(x): '))
        y = int(input('baris(y): '))

        while not (1 <= x <= 3 and 1 <= y <= 3):
            # input x,y harus bilangan diantara 1 dan 3
            print('Kotak tidak valid')
            print('\nGiliran pemain', str(P))
            x = int(input('kolom(x): '))
            y = int(input('baris(y): '))
        
        while papan[y-1][x-1] != ' ':
            # kotak yang diinput tidak boleh sudah berisi
            print('Kotak sudah terisi. Silakan pilih kotak lain.')
            print('\nGiliran pemain', str(P))
            x = int(input('kolom(x): '))
            y = int(input('kolom(y): '))

        # mengisi kotak dengan tanda pemain sesuai giliran
        papan[y-1][x-1] = str(P)

    # ALGORITMA UTAMA
    print("\nLegenda:\n O : Pemain 1\n X : Pemain 2")
    status()

    for i in range(9):
        # mengulangi giliran selama 9 kali
        if i % 2: 
            pemain = 'X'
        else: 
            pemain = 'O'

        giliran(pemain)
        status()
        if menang():
            # jika sudah ada yang menang, hentikan
            print("\nPemain", pemain, "menang secara", menang()[1] + "!")
            break

        if i == 8:
            # belum ada yang menang, tampilkan pesan
            print('\nSeri.')
