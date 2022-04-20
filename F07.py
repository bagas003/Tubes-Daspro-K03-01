import tools

def _urutkan_data(data, skema):
  # Menerima input matriks dan skema pengurutan lalu menghasilkan matriks yang sudah terurut
  n = tools.panjang(data)
  if skema == "harga":
    key = 4
  elif skema == "tahun":
    key = 3
  elif skema == "id":
    key = 0

  temp = [data[i] for i in range(1,n)]; i = 1
  while i < n:
    j = i - 2
    while j >= 0 and data[i][key] < temp[j][key]:
      temp[j+1] = temp[j]
      j -= 1
    temp[j+1] = data[i]
    i += 1

  return temp

def _balikkan_data(data):
  # Menerima input matriks lalu menghasilkan matriks yang terurut terbalik
  return [data[i] for i in range((tools.panjang(data)-1), -1, -1)]



def list_game_toko(data):
  # Akses : user dan admin
  # Menerima input data lalu menampilkan data tersebut dalam kondisi terurut berdasarkan
  # skema pengurutan
  skema = input("Skema sorting : ")

  if skema in ["tahun-", "tahun+", "harga+", "harga-", ''] :
    skema = "id+" if skema == '' else skema
    
    data_terurut = _urutkan_data(data, skema[0:-1])
    if skema[-1] == '-':
      data_terurut = _balikkan_data(data_terurut)
    
    tools.print_data(data_terurut)

  else:
    print("Skema sorting tidak valid!")
