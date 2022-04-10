def login(data):
  # Akses : user dan admin
  # Menerima input data lalu menghasilkan role dan user_id dari user tersebut jika 
  # login berhasil
  username = input("Masukan username: ")
  password = input("Masukan password: ")

  for user in data:
    if user[1] == username and user[3] == password:
      print(f'Halo {user[1]}! Selamat datang di "Binomo".')
      isAdmin = user[4] == 'admin'
      return isAdmin, user[0]
  
  print("Password atau username salah atau tidak ditemukan.")