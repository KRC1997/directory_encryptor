r"""Main module of the single file encryptor."""

# importing standard modules --------------------------------------------------
import sys

# importing third-party modules -----------------------------------------------
from cryptography.fernet import Fernet

# importing custom modules ----------------------------------------------------


def print_help_text() -> None:
    r"""Prints help text to console."""
    help_text: str = "\
        Valid options:\
            -encrypt or -e [path/to/file]\
            -decrypt or -d [path/to/file] [key]"
    print(help_text)
    return


def encrypt(full_file_path: str) -> None:
    r"""encrypts the given file and writes the key to console"""
    key = Fernet.generate_key()

    print("Key Value used: {}".format(key))

    f = Fernet(key)
    with open(full_file_path, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open ("encrypt.xyz", 'wb') as file:
        file.write(encrypted)

    return None

def decrypt(full_file_path: str, key: str) -> None:
    f = Fernet(key)

    print("Note that you must know what type of file it is in advance :P")

    with open(full_file_path, 'rb') as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open("decrypt.xyz", 'wb') as file:
        file.write(decrypted)

    return None


if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print_help_text()
        raise ValueError("Expected an option and related parameters")
    
    if sys.argv[1] == "-encrypt" or sys.argv[1] == "-e":
        encrypt(sys.argv[2])
    elif sys.argv[1] == "-decrypt" or sys.argv[1] == "-d":
        decrypt(sys.argv[2], sys.argv[3])
