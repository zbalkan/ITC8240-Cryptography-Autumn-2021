class TransmissionCipher:
    def __init__(self):
        print("An instance of class TransmissionCipher is initiated.")

    def __str__(self):
        return "Encrypt/decrypt text with Transmission Cipher."

    #region Public Methods
    def encrypt(self, plain_text:str, key: str, padding: str) -> str:
        # Get rid of spaces and just for cosmetics, set them as lowercase
        plain_text = plain_text.replace(" ","").lower()

        # Added padding at the end so that dividing the actual message would be easier
        modulus = len(plain_text) % len(key)
        if(modulus != 0):
            number_of_padding = len(key) - modulus
            for _ in range (0, number_of_padding):
                plain_text += padding
        internal_cipher_text = ""

        # Divide the message in blocks with the same size of the key
        for first_index_of_block in range(0, (len(plain_text)), len(key)):
            last_index_of_block = (first_index_of_block + len(key))
            text_block = plain_text[first_index_of_block: last_index_of_block]

            # For each block, modify the characters by the key
            new_text_block = ""
            for j in range(0, len(key)):
                order = int(key[j]) - 1
                new_text_block += text_block[order]

            internal_cipher_text += new_text_block

        return internal_cipher_text
    #endregion
