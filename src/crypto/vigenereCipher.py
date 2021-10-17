class VigenereCipher:

    def __init__(self):
        print("An instance of class ", type(self).__name__, " is initiated.")

    def __str__(self):
        return "Encrypt/decrypt text with Vigenere Cipher."

    #region Public Methods
    def encrypt(self, plain_text : str, key : str) -> str:
        alphabet_length = 26
        plain_text = plain_text.replace(" ","").upper()

        new_key = self.__adjust_key(plain_text, key)

        # start encrypting
        cipher_text = ""
        for i in range(0, len(plain_text)):
            plain_text_char_as_int = self.__ord_ascii(plain_text[i])
            offset = self.__ord_ascii(new_key[i])
            cipher_text += self.__chr_ascii((plain_text_char_as_int + offset) % alphabet_length)
        return cipher_text
    #endregion

    #region Private Methods
    def __adjust_key(self, plain_text : str, key : str):
        # modify the key to match the length of the plain text
        # use uppercase for ease of use in ASCII
        adjusted_key = ""
        if(len(plain_text) <= len(key)):
            adjusted_key = key.upper()
        else:
            for i in range(0, len(plain_text)):
                adjusted_key += key[i % len(key)].upper()
        return adjusted_key

    def __ord_ascii(self, character : chr) -> int:
        return ord(character) - 65

    def __chr_ascii(self, integer: int) -> chr:
        return chr(integer + 65)
    #endregion
