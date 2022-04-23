# F17 - Exit

def exit():
    # konfirmasi apakah pengguna ingin menyimpan perubahan atau tidak
    # I.S. menerima masukan konfirmasi pengguna
    # F.S. mengembalikan True jika pengguna hendak menyimpan data atau sebaliknya

    # KAMUS LOKAL
    # simpan : char

    # ALGORITMA
    # input konfirmasi
    simpan = input('\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    # validasi input
    while not (simpan == 'Y' or simpan == 'y' or simpan == 'N' or simpan == 'n'):
        simpan = input('\nApakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    # mengembalikan nilai boolean yang sesuai
    if simpan == 'Y' or simpan == 'y': 
        return True
    else:
        return False
    
    
