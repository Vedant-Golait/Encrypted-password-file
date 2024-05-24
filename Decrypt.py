from cryptography.fernet import Fernet

# -------------- Reads the Key ---------------

with open("Code\mykey.key", "rb") as mykey:
    key=mykey.read()

# ----------------Decrypt the  file---------------------



f = Fernet(key)

with open("Code\enc_passwords.txt", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open ("Code\dec_passwords.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted)


