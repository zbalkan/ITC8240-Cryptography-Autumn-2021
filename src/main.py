if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.abspath(__file__) ) )
        from crypto.caesarCipher import CaesarCipher
        from crypto.transmissionCipher import TransmissionCipher
        from crypto.vigenereCipher import VigenereCipher
        from crypto.indexOfCoincidence import IndexOfCoincidence
    else:
        from .crypto.caesarCipher import CaesarCipher
        from .crypto.transmissionCipher import TransmissionCipher
        from .crypto.vigenereCipher import VigenereCipher
        from .crypto.indexOfCoincidence import IndexOfCoincidence

#region Tasks
def task_1(caesar : CaesarCipher, transmission : TransmissionCipher) -> None:
    plaintext = "BLOCKCHAIN"

    temp = caesar.encrypt(plain_text= plaintext, key=9) # S1
    temp = transmission.encrypt(plain_text= temp, key= '51324',padding='x') # P1
    temp = caesar.encrypt(plain_text= temp, key= 19) # S2
    ciphertext = transmission.encrypt(plain_text= temp, key='31425', padding='x') # P2

    print('Task 1:')
    print(ciphertext)

def task_2(vigenere : VigenereCipher, ioc :IndexOfCoincidence) -> None:
    plaintext = 'FRIENDSMAKETHEWORSTENEMIES'
    key = 'list'

    ciphertext = vigenere.encrypt(plain_text= plaintext, key= key)
    print('Task 2:')
    print('1. ' , ciphertext)
    print('2. ' , ioc.calculate(text= plaintext))
    print('3. ' , ioc.calculate(text= ciphertext))

#endregion

def main():
    caesar = CaesarCipher()
    transmission  = TransmissionCipher()
    vigenere = VigenereCipher()
    ioc = IndexOfCoincidence()

    task_1(caesar= caesar, transmission= transmission)
    task_2(vigenere= vigenere, ioc= ioc)

if __name__ == "__main__":
    main()

