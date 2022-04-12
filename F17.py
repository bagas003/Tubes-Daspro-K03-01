def exit():
    simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    while simpan not in ('y', 'Y', 'n', 'N'):
        simpan = input('Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ')

    if simpan in ('y', 'Y'): return True
    
    return False
    
    
