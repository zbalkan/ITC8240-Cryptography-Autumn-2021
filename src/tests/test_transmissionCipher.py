import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.transmissionCipher import TransmissionCipher
    else:
        from ..crypto.transmissionCipher import TransmissionCipher

class test_transmission_cipher(unittest.TestCase):
    def test_encrypt_transm(self):
        transmission = TransmissionCipher()
        result = transmission.encrypt("Mathematics is a language","5174632", "x")
        self.assertEqual(result, "emahmtaitassciulgganaxexxxxx") # Should be emahmtaitassciulgganaxexxxxx

if __name__ == '__main__':
        unittest.main()
