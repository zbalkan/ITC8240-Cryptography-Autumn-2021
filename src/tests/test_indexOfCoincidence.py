import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.indexOfCoincidence import IndexOfCoincidence
    else:
        from ..crypto.indexOfCoincidence import IndexOfCoincidence

class test_index_of_coincidence(unittest.TestCase):
    def test_encrypt_indexOfCoincidence(self):
        ioc = IndexOfCoincidence()
        result = ioc.calculate_index_of_coincidence("EPYEPOPDZSZUFPO")
        self.assertEqual(result, 0.08571428571428572) # Should be 0.08571428571428572

if __name__ == '__main__':
        unittest.main()
