#region Public Methods
def encrypt_caesar( plain_text:str, key: int) -> str:
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

def decrypt_caesar( cipher_text:str, key: int) -> str:
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

#region Tests
result = encrypt_caesar("mor ni ng", 11) # should return XZCYTYR, added spaces just to check
if(result == "XZCYTYR"):
    print("pass")
else:
    print("fail")

result = decrypt_caesar("XZCYTYR", 11) # should return MORNING
if(result == "MORNING"):
    print("pass")
else:
    print("fail")
#endregion
