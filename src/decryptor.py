r"""This module exposes the 'decrypt' function that performs decryption for a
given file. It also contains other functions that are used by the module
internally."""


# importing standard modules --------------------------------------------------


# making sure that only "encrypt" is exported when importing *
__all__ = ["decrypt"]


def decrypt(
    target_file_name: str,
    pswd_string: str, 
    destination_path: str,
    ) -> bool:
    r"""Decrypts a given file and places the contents in it at the 
    'destination_path'."""
    raise NotImplementedError("Function yet to be implemented")


