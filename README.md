# Password Encryption and Decryption Tool

This Python project provides a simple tool to encrypt and decrypt passwords using the Fernet encryption algorithm from the `cryptography` library. It allows you to securely store your passwords in an encrypted format and retrieve them when needed.

## Features

- Generate a secure encryption key
- Encrypt a plaintext file containing passwords
- Decrypt an encrypted file to retrieve the original passwords

## Prerequisites

- Python 3.x
- `cryptography` library (install with `pip install cryptography`)

## Usage

1. Generate a new encryption key by running the `Gen_key.py` script. This will create a `mykey.key` file in the `Code` directory.

2. To encrypt your passwords, run the `Encrypt.py` script. It will prompt you to enter various passwords (Facebook, Instagram, Google, LinkedIn, Twitter, and others). The script will create a `passwords.txt` file in the `Code` directory with your entered passwords, and then encrypt it to generate an `enc_passwords.txt` file.

3. To decrypt the encrypted passwords file, run the `Decrypt.py` script. It will use the `mykey.key` file to decrypt the `enc_passwords.txt` file and create a `dec_passwords.txt` file with the original plaintext passwords.

## File Structure

```
project_directory/
├── Code/
│   ├── mykey.key (generated encryption key)
│   ├── passwords.txt (plaintext passwords file)
│   ├── enc_passwords.txt (encrypted passwords file)
│   └── dec_passwords.txt (decrypted passwords file)
├── Decrypt.py (Decryption)
├── Encrypt.py (Encryption)
├── Gen_key.py (Key Generation)
└── README.md
```

## Note

- Keep your encryption key (`mykey.key`) safe and secure, as it is required for both encryption and decryption.
- Do not share your encrypted password files (`enc_passwords.txt`) with others, as they can be decrypted with the corresponding encryption key.

## License

This project is licensed under the [MIT License](LICENSE).
