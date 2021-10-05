import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.vigenereCipher import VigenereCipher
    else:
        from ..crypto.vigenereCipher import VigenereCipher

class test_vigenere_cipher(unittest.TestCase):
    def test_encrypt_vigenere(self):
        vigenere = VigenereCipher()
        result = vigenere.encrypt("PARADOX", "YESTERDAY")
        self.assertEqual(result, "NEJTHFA") # Should be NEJTHFA

if __name__ == '__main__':
        unittest.main()
