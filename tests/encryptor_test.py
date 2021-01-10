r"""Unit test script for 'encryptor' module"""

# importing standard modules --------------------------------------------------
import unittest


# importing custom modules ----------------------------------------------------
import encryptor


# Test Suite Definition -------------------------------------------------------
class TestEncryptor(unittest.TestCase):

    def test_encrypt(self):
        with self.assertRaises(NotImplementedError):
            encryptor.encrypt("kunal", "kunal", "kunal")
        pass

    pass # end of class TestEncryptor(unittest.TestCase) definition


# Run the test suite ----------------------------------------------------------
if __name__ == '__main__':
    unittest.main(verbosity=2)

    # Notes:
    # 1) 'verbosity=2' is eqivalent to passing '-v' option to the script in the
    # command line interface for more detailed reports from unittest.main()
