from cryptography.fernet import Fernet


#  ---------------To open a key sent from someone---------------
with open(r"Code\mykey.key", 'r') as mykey:                #opens the key
    key = mykey.read()                          #reads the key

print("Here is the key we will be using to encrypt your files : \n \t ",key)


# ------------------Encrypt a file using the key-----------------
passwords = r"Code\passwords.txt"
print("Enter the password for the file:")  #asks for the password
passwords_FB = input("Facebook: ")
passwords_IG = input("Instagram: ")
passwords_G = input("Google: ")
passwords_L = input("Linkedin: ")
passwords_T = input("Twitter: ")

a = input("Do You want to add more passwords?\nAnswer with 'yes' or 'no': ")
if a.lower() == "yes":
    # ---------------------------------other password loop----------------
    passwords_other = []
    add_more = True

    while add_more:
        other_password = input("Enter other password (or 'q' to quit): ")
        if other_password.lower() == 'q':
            add_more = False
        else:
            passwords_other.append(other_password)

# --------------------------- write passwords in password.txt-------------
with open(passwords, 'w') as f:
    f.write("Facebook: " + passwords_FB + "\n")
    f.write("Instagram: " + passwords_IG + "\n")
    f.write("Google: " + passwords_G + "\n")
    f.write("Linkedin: " + passwords_L + "\n")
    f.write("Twitter: " + passwords_T + "\n")
    for pwd in passwords_other:
        f.write("Other: " + pwd + "\n")


#  --------------------------Encrypt the file-----------------


f = Fernet(key)
with open(r"Code\passwords.txt", "r") as passlist:
    original = passlist.read()  #reads the file

encrypted = f.encrypt(original.encode())

with open(r"Code\enc_passwords.txt", 'wb') as encrypted_file:  #writes the encrypted file
    encrypted_file.write(encrypted)