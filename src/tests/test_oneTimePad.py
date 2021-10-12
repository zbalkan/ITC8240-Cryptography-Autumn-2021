import unittest

if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.oneTimePad import OneTimePad
    else:
        from ..crypto.oneTimePad import OneTimePad

class test_one_time_pad(unittest.TestCase):
    def test_encode_binary(self):
        otp = OneTimePad()
        result = otp.encode_binary('CAT')
        self.assertEqual(result, '000100000010011') # Should be 000100000010011

    def test_decode_binary(self):
        otp = OneTimePad()
        result = otp.decode_binary('000100000010011')
        self.assertEqual(result, 'CAT') # Should be CAT

    def test_calculate_key(self):
        otp = OneTimePad()
        result = otp.calculate_key(plain_text= 'DOUGH', cipher_text= '1000000110001010001000100')
        self.assertEqual(result, 'TIRED')

if __name__ == '__main__':
        unittest.main()
