import B01

def login(data):
  # Akses : user dan admin
  # Menerima input data user lalu menghasilkan role dan user_id dari user tersebut jika 
  # login berhasil, serta menghasilkan status apakah login berhasil
  username = input("Masukan username: ")
  password = input("Masukan password: ")

  password = B01.encrypt(password, "daspro")

  for user in data:
    if user[1] == username and user[3] == password:
      print(f'Halo {user[1]}! Selamat datang di "Binomo".')
      isAdmin = user[4] == 'admin'
      return True, isAdmin, user[0]
  
  print("Password atau username salah atau tidak ditemukan.")
  return False, False, 0

