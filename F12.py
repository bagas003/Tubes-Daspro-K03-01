# F12 - Top Up Saldo
import tools

def topup(data_user):
    # menambahkan saldo kepada user 
    # I.S. pengguna sudah login dan matriks data file user terdefinisi
    # F.S. saldo berhasil ditambahkan ke database

    # KAMUS LOKAL
    # input_username : string
    # input_saldo : int
    # isUsernameValid : boolean

    # ALGORITMA
    input_username = input("Masukan username: ")
    input_saldo = int(input("Masukan saldo: "))

    # Validasi username
    isUsernameValid = False
    for i in range(tools.panjang(data_user)):
        if (data_user[i][1] == input_username):
            isUsernameValid = True
            break

    if not isUsernameValid:
        print("Username " + '"' + input_username + '"' + " tidak ditemukan")
    else: #isUsernameValid
        if ((int(data_user[i][5]) + input_saldo) < 0): 
            print("Masukan tidak valid.") 
        else: # (data_user[i][5] + input_saldo) >= 0
            data_user[i][5] = str(int(data_user[i][5]) + input_saldo)
            if (input_saldo > 0):
                print("Top up berhasil. Saldo",data_user[i][2],"bertambah menjadi",data_user[i][5])
            elif (input_saldo < 0):
                print("Top up berhasil. Saldo",data_user[i][2],"berkurang menjadi",data_user[i][5])
            else: # asumsi input_saldo != 0
                print("Masukan tidak valid")
    return data_user
