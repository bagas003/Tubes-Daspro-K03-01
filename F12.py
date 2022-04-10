# F12 - Top Up Saldo
def topup():
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
    for i in range(len(user)):
        if (user[i][1] == input_username):
            isUsernameValid = True
            break

    if isUsernameValid == False:
        print("Username " + '"' + input_username + '"' + " tidak ditemukan")
    else: #isUsernameValid = True
        if ((user[i][5] + input_saldo) < 0): 
            print("Masukan tidak valid.") 
        else: # (user[i][5] + input_saldo) >= 0
            user[i][5] += input_saldo
            if (input_saldo > 0):
                print("Top up berhasil. Saldo",user[i][2],"bertambah menjadi",user[i][5])
            elif (input_saldo < 0):
                print("Top up berhasil. Saldo",user[i][2],"berkurang menjadi",user[i][5])
            else: # asumsi input_saldo != 0
                print("Masukan tidak valid")

# PROGRAM UTAMA

# KAMUS GLOBAL
# type data_user : <id: string, username: string, nama: string, alamat: string, password: int, role: string>
# user : array of data_user
# isAdmin, isProgramValid : boolean
# menu : string

# INISIALISASI
# Note : data dibawah ini hanya digunakan untuk mengetes jalannya program
# ketika nanti digabung, diabaikan saja.
user = [['id','username','nama','password','role','saldo'],
        [1,'bagas012','bagas aryo seto',16521012,'admin',1000],
        [2,'fahia057','fahia ali anwari',16521057,'admin',1000],
        [3,'rava102','rava maulana azzikri',16521102,'admin',1000],
        [4,'albert192','albert',16521192,'admin',1000]]

# ALGORITMA
isProgramValid = True
# contohnya isAdmin merupakan variabel yang direturn dari fungsi login
isAdmin = False

while isProgramValid:
    menu = input()
    if menu == "topup":
        topup()
    else:
        exit()

