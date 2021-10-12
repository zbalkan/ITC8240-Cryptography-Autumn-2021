class OneTimePad:

    def __init__(self):
        print('An instance of class ', type(self).__name__,' is initiated.')

    def __str__(self):
        return "Encode/decode, encrypt/decrypt text with OneTimePad."

    #region Public methods
    def encrypt(self, plain_text : str, binary_key : str) -> str:
        encoded_text = self.encode_binary(plain_text)
        cipher_text = int(encoded_text, 2) ^ int(binary_key, 2)
        return cipher_text

    def decrypt(self, cipher_text : str, binary_key : str) -> str:
        int_xor_result = int(cipher_text, 2) ^ int(binary_key, 2)
        binary_xor_result = self.__int_to_bin_fixed(int_xor_result)
        plain_text = self.decode_binary(binary_xor_result)
        return plain_text

    def calculate_key(self, plain_text: str, cipher_text : str) -> str:
        int_xor_result = int(self.encode_binary(plain_text), 2) ^ int(cipher_text, 2)
        binary_xor_result = self.__int_to_bin_fixed(int_xor_result)
        binary_key = self.decode_binary(binary_xor_result)
        return binary_key

    def encode_binary(self, plain_text: str) -> str:
        plain_text = plain_text.upper()
        cipher_text = ''
        for char in plain_text:
            cipher_text += (self.__convert_to_binary(character = char))
        return cipher_text

    def decode_binary(self, binary_text : str) -> str:
        plain_text = ''

        # Divide the message in blocks with 5, the fixed-length of binary strings
        for first_index_of_block in range(0, (len(binary_text)), 5):
            last_index_of_block = (first_index_of_block + 5)
            binary_char = binary_text[first_index_of_block: last_index_of_block]

            # For each text block (a binary char), convert binary string to equivalent chr
            plain_text += (self.__convert_to_chr(binary_char))

        return plain_text
    #endregion

    #region Private Methods
    def __convert_to_binary(self, character : chr) -> str:
        return self.__int_to_bin_fixed(self.__ord_ascii(character)) # 5-char fixed length binary as string

    def __convert_to_chr(self, binary : str) -> chr:
        return self.__chr_ascii(int(binary, 2))

    def __ord_ascii(self, character : chr) -> int:
        return ord(character) - 65

    def __chr_ascii(self, integer: int) -> chr:
        return chr(integer + 65)

    def __int_to_bin_fixed(self, number : int) -> str:
        return '{0:05b}'.format(number)
    #endregion
