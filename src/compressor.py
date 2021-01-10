r"""This module contains functions to help in compressing and decompressing 
the target directory.
"""


# importing standard modules --------------------------------------------------
import shutil


# making sure that only "compress_directory" is exported when importing *
__all__ = ["compress_directory"]


def compress_directory(
    target_directory_path: str,
    target_file_name: str, 
    # will be appended with the appropriate extension by the function
    target_destination_directory: str = None
    # if none, then it will place it 
    ) -> None:
    r"""This function performs the compression operation on the given directory.
    """
    raise NotImplementedError("Function yet to be implemented")
