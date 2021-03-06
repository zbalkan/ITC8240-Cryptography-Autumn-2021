import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.affineCipher import AffineCipher
    else:
        from ..crypto.affineCipher import AffineCipher

class test_affine_cipher(unittest.TestCase):
    def test_encrypt(self):
        affine = AffineCipher()
        result = affine.encrypt(plain_text="message", a= 7, b= 13)
        self.assertEqual(result, "TPJJNDP") # Should be TPJJNDP

    def test_decrypt_with_encryption_key(self):
        affine = AffineCipher()
        result = affine.decrypt_with_encryption_key(cipher_text="TPJJNDP", a= 7, b= 13)
        self.assertEqual(result , "MESSAGE") # Should be MESSAGE

    def test_decrypt_with_decryption_key(self):
        affine = AffineCipher()
        result = affine.decrypt_with_decryption_key(cipher_text="TPJJNDP", a_inv= 15, b= 13)
        self.assertEqual(result , "MESSAGE") # Should be MESSAGE

    def test_calculate_encryption_cipher(self):
        affine = AffineCipher()
        result = affine.calculate_encryption_key(plain_text= 'SURFACE', cipher_text= 'NJCAXTP')
        self.assertEqual(result, '11 * (x + 23) mod 26')

    def test_calculate_decryption_cipher(self):
        affine = AffineCipher()
        result = affine.calculate_decryption_key(plain_text= 'SURFACE', cipher_text= 'NJCAXTP')
        self.assertEqual(result, '19 * (x + 23) mod 26')

if __name__ == '__main__':
        unittest.main()
