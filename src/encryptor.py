r"""This module exposes the 'encrypt' function that performs encryption for a
given file. It also contains other functions that are used by the module
internally."""


# importing standard modules --------------------------------------------------


# making sure that only "encrypt" is exported when importing *
__all__ = ["encrypt"]


def encrypt(
    target_file_name: str,
    pswd_string: str, 
    destination_path: str,
    ) -> bool:
    r"""Encrypts a given file and places it in the 'destination_path'"""
    raise NotImplementedError("Function yet to be implemented")


