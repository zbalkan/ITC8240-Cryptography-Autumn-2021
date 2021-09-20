#region Private Methods
def __calculate_affine_encryption(x: chr, a: int, b: int) -> chr:
    first_number = ord("A") # first ascii char to print
    length_of_alphabet = 26 # No to magic numbers

    # a*(x + b) mod m
    integer = (a * (ord(x) - first_number) + b) % length_of_alphabet
    return chr(integer + first_number)


def __calculate_inverse_a(a: int) -> int:
    length_of_alphabet = 26 # No to magic numbers
    a_inverse = 0

    # find a number that (a * a^-1) mod m = 1
    for i in range (0, length_of_alphabet):
        if (((a * i) % 26) == 1):
            a_inverse = i

    return a_inverse

def __calculate_affine_decryption_with_encryption_key(x: chr, a: int, b:int) -> chr:
    first_number = ord("A") # first ascii char to print
    length_of_alphabet = 26 # No to magic numbers
    a_inv = __calculate_inverse_a(a)

    # a^-1 ( x - b ) mod m
    return chr((a_inv * ( (ord(x) - first_number)- b) % length_of_alphabet) + first_number)

def __calculate_affine_decryption_with_decryption_key(x: chr, a_inv: int, b:int) -> chr:
    first_number = ord("A") # first ascii char to print
    length_of_alphabet = 26

    # a^-1 ( x - b ) mod m
    return chr((a_inv * ( (ord(x) - first_number)- b) % length_of_alphabet) + first_number)
#endregion

#region Public Methods
def encrypt_affine(plain_text: str, a: int, b: int) -> str:
    plain_text = plain_text.replace(" ","").upper()
    cipher_text = ""

    for index in range (0, len(plain_text)):
        cipher_text += __calculate_affine_encryption(x= plain_text[index], a= a, b= b)

    return cipher_text

def decrypt_affine_with_encryption_key(cipher_text: str,a:int,b:int) -> str:
    cipher_text = cipher_text.replace(" ","").upper()
    plain_text = ""

    for index in range (0, len(cipher_text)):
        plain_text += __calculate_affine_decryption_with_encryption_key(cipher_text[index],a,b)

    return plain_text

def decrypt_affine_with_decryption_key(cipher_text: str, a_inv:int,b:int) -> str:
    cipher_text = cipher_text.replace(" ","").upper()
    plain_text = ""

    for index in range (0, len(cipher_text)):
        plain_text += __calculate_affine_decryption_with_decryption_key(x= cipher_text[index], a_inv= a_inv, b= b)

    return plain_text
#endregion

#region Tests
result = encrypt_affine(plain_text="message", a= 7, b= 13)
if(result == "TPJJNDP"):
    print("pass")
else:
    print("fail")

result = decrypt_affine_with_encryption_key(cipher_text="TPJJNDP", a= 7, b= 13)
if(result == "MESSAGE"):
    print("pass")
else:
    print("fail")

result = __calculate_inverse_a(7)
if(result == 15):
    print("pass")
else:
    print("fail")

result = decrypt_affine_with_decryption_key(cipher_text="TPJJNDP", a_inv= 15, b= 13)
if(result == "MESSAGE"):
    print("pass")
else:
    print("fail")
#endregion


print(encrypt_affine("symbol",3,2))
