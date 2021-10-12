if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from crypto.caesarCipher import CaesarCipher
        from crypto.transmissionCipher import TransmissionCipher
    else:
        from .crypto.caesarCipher import CaesarCipher
        from .crypto.transmissionCipher import TransmissionCipher

#region Tasks
def task_1(caesar : CaesarCipher, transmission : TransmissionCipher) -> None:
    plaintext = "BLOCKCHAIN"


    temp = caesar.encrypt(plain_text= plaintext, key=9) # S1
    temp = transmission.encrypt(plain_text= temp, key= '51324',padding='x') # P1
    temp = caesar.encrypt(plain_text= temp, key= 19) # S2
    ciphertext = transmission.encrypt(plain_text= temp, key='31425', padding='x') # P2

    print(ciphertext)


#endregion

def main():
    caesar = CaesarCipher()
    transmission  = TransmissionCipher()

    task_1(caesar= caesar, transmission= transmission)

if __name__ == "__main__":
    main()

