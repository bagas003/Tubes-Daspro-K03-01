def exit():
    simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    while simpan != 'Y' or 'y' or 'N' or 'n':
        simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    if simpan == 'Y' or 'y': return True
    else: return False
    
    