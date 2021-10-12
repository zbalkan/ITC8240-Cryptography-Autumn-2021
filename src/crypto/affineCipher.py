class AffineCipher:
    def __init__(self):
        print("An instance of class AffineCipher is initiated.")

    def __str__(self):
        return "Encrypt/decrypt text with Affine Cipher."

    #region Public Methods
    def encrypt(self, plain_text: str, a: int, b: int) -> str:
        plain_text = plain_text.replace(" ","").upper()
        cipher_text = ""

        for index in range (0, len(plain_text)):
            cipher_text += self.__calculate_affine_encryption(x= plain_text[index], a= a, b= b)

        return cipher_text

    def decrypt_with_encryption_key(self, cipher_text: str,a:int,b:int) -> str:
        cipher_text = cipher_text.replace(" ","").upper()
        plain_text = ""

        for index in range (0, len(cipher_text)):
            plain_text += self.__calculate_affine_decryption_with_encryption_key(cipher_text[index],a,b)

        return plain_text

    def decrypt_with_decryption_key(self, cipher_text: str, a_inv:int,b:int) -> str:
        cipher_text = cipher_text.replace(" ","").upper()
        plain_text = ""

        for index in range (0, len(cipher_text)):
            plain_text += self.__calculate_affine_decryption_with_decryption_key(x= cipher_text[index], a_inv= a_inv, b= b)

        return plain_text

    def calculate_encryption_key(self, plain_text : str, cipher_text : str) -> str:
        for a in range(1, 26, 1):
            for b in range(1,26,1):
                temp = self.encrypt(plain_text, a, b)
                if(temp.lower() == cipher_text.lower()):
                    encryption_key = ''.join([str(a), ' * (x + ', str(b),') mod 26'])
                    break

        return encryption_key

    def calculate_decryption_key(self, plain_text : str, cipher_text : str) -> str:
        for a in range(1, 26, 1):
            for b in range(1,26,1):
                temp = self.encrypt(plain_text, a, b)
                if(temp.lower() == cipher_text.lower()):
                    a_inv = self.__calculate_inverse_a(a= a)
                    decryption_key = ''.join([str(a_inv), ' * (x + ', str(b),') mod 26'])
                    break

        return decryption_key
    #endregion

    #region Private Methods
    def __calculate_affine_encryption(self, x: chr, a: int, b: int) -> chr:
        first_number = ord("A") # first ascii char to print
        length_of_alphabet = 26 # No to magic numbers

        # a*(x + b) mod m
        integer = (a * (ord(x) - first_number) + b) % length_of_alphabet
        return chr(integer + first_number)


    def __calculate_inverse_a(self, a: int) -> int:
        length_of_alphabet = 26 # No to magic numbers
        a_inverse = 0

        # find a number that (a * a^-1) mod m = 1
        for i in range (0, length_of_alphabet):
            if (((a * i) % 26) == 1):
                a_inverse = i
        return a_inverse

    def __calculate_affine_decryption_with_encryption_key(self, x: chr, a: int, b:int) -> chr:
        first_number = ord("A") # first ascii char to print
        length_of_alphabet = 26 # No to magic numbers
        a_inv = self.__calculate_inverse_a(a)

        # a^-1 ( x - b ) mod m
        return chr((a_inv * ( (ord(x) - first_number)- b) % length_of_alphabet) + first_number)

    def __calculate_affine_decryption_with_decryption_key(self, x: chr, a_inv: int, b:int) -> chr:
        first_number = ord("A") # first ascii char to print
        length_of_alphabet = 26

        # a^-1 ( x - b ) mod m
        return chr((a_inv * ( (ord(x) - first_number)- b) % length_of_alphabet) + first_number)
    #endregion
