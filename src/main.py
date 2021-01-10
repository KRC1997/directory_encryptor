r"""Main entry point of the program."""

# importing standard modules --------------------------------------------------
import sys


# importing custom modules ----------------------------------------------------
import compressor
import decryptor
import encryptor


def main(argv: list) -> int:
    r"""Customary Main Function \
    argv : list : command line argument list"""

    if len(argv) == 0:
        error_message: str = """Expected arguments as follows:
encrypt <directory_path> <destination_file_name> <destination_path>
decrypt <target_file_name> <destination_path>"""
        raise ValueError(error_message)


    raise NotImplementedError("Function yet to be implemented")


if __name__ == "__main__":
    # Obtain and parse arguments from command line
    # perform corresponding actions
    try:
        main(sys.argv[1:])
    except Exception as error:
        print(type(error), error)
    finally:
        print(" -- execution complete -- ")
