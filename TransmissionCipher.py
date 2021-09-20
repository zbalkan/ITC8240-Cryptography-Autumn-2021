#region Public Methods
def encrypt_transmission( plain_text:str, key: str, padding: str) -> str:
    plain_text = plain_text.replace(" ","").lower()

    modulus = len(plain_text) % len(key)
    if(modulus != 0):
        number_of_padding = len(key) - modulus
        for p in range (0, number_of_padding):
            plain_text += padding
    internal_cipher_text = ""

    for first_index_of_block in range(0, (len(plain_text)), len(key)):
        last_index_of_block = (first_index_of_block + len(key))
        text_block = plain_text[first_index_of_block: last_index_of_block]

        new_text_block = ""
        for j in range(0, len(key)):
            order = int(key[j]) - 1
            new_text_block += text_block[order]

        internal_cipher_text += new_text_block

    return internal_cipher_text
#endregion

#region Tests
result = encrypt_transmission("Mathematics is a language","5174632", "x")
if(result == "emahmtaitassciulgganaxexxxxx"):
    print("pass")
else:
    print("fail")
#endregion
