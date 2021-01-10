r"""Unit test script for 'compressor' module"""

# importing standard modules --------------------------------------------------
import unittest


# importing custom modules ----------------------------------------------------
import compressor


# Test Suite Definition -------------------------------------------------------
class TestCompressor(unittest.TestCase):

    def test_compress_directory(self):
        with self.assertRaises(NotImplementedError):
            compressor.compress_directory("kunal", "kunal", "kunal")
        pass

    pass # end of class TestCompressor(unittest.TestCase): definition


# Run the test suite ----------------------------------------------------------
if __name__ == '__main__':
    unittest.main(verbosity=2)

    # Notes:
    # 1) 'verbosity=2' is eqivalent to passing '-v' option to the script in the
    # command line interface for more detailed reports from unittest.main()
