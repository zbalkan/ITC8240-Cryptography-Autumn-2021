#region Private Methods
def __adjust_key(plain_text : str, key : str):
    # modify the key to match the length of the plain text
    # use uppercase for ease of use in ASCII
    adjusted_key = ""
    if(len(plain_text) <= len(key)):
        adjusted_key = key.upper()
    else:
        for i in range(0, len(plain_text)):
            adjusted_key += key[i % len(key)].upper()
    return adjusted_key
#endregion

#region Public Methods
def encrypt_vigenere(plain_text : str, key : str) -> str:
    alphabet_length = 26
    plain_text = plain_text.replace(" ","").upper()

    new_key = __adjust_key(plain_text, key)

    # start encrypting
    cipher_text = ""
    for i in range(0, len(plain_text)):
        plain_text_char_as_int = ord(plain_text[i]) - 65
        offset = ord(new_key[i]) - 65
        cipher_text_char_as_int = (plain_text_char_as_int + offset) % alphabet_length + 65
        cipher_text += chr(cipher_text_char_as_int)
    return cipher_text
#endregion

#region Tests
result = encrypt_vigenere("PARADOX", "YESTERDAY")
if(result == "NEJTHFA"):
    print("pass")
else:
    print("fail")
#endregion
