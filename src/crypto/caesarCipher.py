class CaesarCipher:

    def __init__(self):
        print("An instance of class ', type(self).__name__,' is initiated.")

    def __str__(self):
        return "Encrypt/decrypt text with Caesar (Shift) Cipher."

    #region Public Methods
    def encrypt (self, plain_text: str, key: int) -> str:
        alphabet_length = 26
        plain_text = plain_text.replace(" ","").upper()
        key = key % alphabet_length

        internal_cipher_text = ""
        for character in  plain_text:
            char_as_int = ord(character)
            char_as_int += key
            if (char_as_int > 90):
                char_as_int -= alphabet_length
            character = chr(char_as_int)
            internal_cipher_text += character

        return internal_cipher_text

    def decrypt (self, cipher_text: str, key: int) -> str:
        alphabet_length = 26
        cipher_text = cipher_text.upper()
        key = key % alphabet_length

        internal_plain_text = ""
        for character in  cipher_text:
            char_as_int = ord(character)
            char_as_int -= key
            if (char_as_int < 65):
                char_as_int += alphabet_length
            character = chr(char_as_int)
            internal_plain_text += character

        return internal_plain_text
    #endregion
