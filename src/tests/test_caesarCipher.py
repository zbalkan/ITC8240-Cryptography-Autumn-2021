import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.caesarCipher import CaesarCipher
    else:
        from ..crypto.caesarCipher import CaesarCipher

class test_caesar_cipher(unittest.TestCase):
    def test_encrypt_caesar(self):
        caesar = CaesarCipher()
        result = caesar.encrypt("mor ni ng", 11)
        self.assertEqual(result, "XZCYTYR") # Should be XZCYTYR


    def test_decrypt_caesar(self):
        caesar = CaesarCipher()
        result = caesar.decrypt("XZCYTYR", 11)
        self.assertEqual(result , "MORNING") # Should be MORNING

if __name__ == '__main__':
        unittest.main()
