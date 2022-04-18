# Vigenere cipher

def _buat_key(pesan, key):
  hasil = key
  for i in range(len(pesan) - len(key)):
    hasil += key[i % len(key)]
  return hasil

def encrypt(pesan, key):
  key = _buat_key(pesan, key)
  hasil = ""
  for i in range(len(pesan)):
    x = ord(pesan[i]) + ord(key[i]) - 66
    x = x % 93 + 33
    hasil += chr(x)
  return hasil

def decrypt(pesan, key):
  key = _buat_key(pesan, key)
  hasil = ""
  for i in range(len(pesan)):
    x = ord(pesan[i]) - ord(key[i])
    x = x % 93 + 33
    hasil += chr(x)
  return hasil