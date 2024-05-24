from cryptography.fernet import Fernet

# --------------------------To generate a Key---------------

key =  Fernet.generate_key() #generates a key
with open("code\mykey.key",'wb') as mykey: #writes the key to a file
    mykey.write(key)
