if __name__ == '__main__':
    if __package__ == '':
        import sys
        from os import path
        sys.path.append( path.dirname( path.abspath(__file__) ) )
        from crypto.caesarCipher import CaesarCipher
        from crypto.transmissionCipher import TransmissionCipher
        from crypto.vigenereCipher import VigenereCipher
        from crypto.indexOfCoincidence import IndexOfCoincidence
        from crypto.affineCipher import AffineCipher
        from crypto.oneTimePad import OneTimePad
    else:
        from .crypto.caesarCipher import CaesarCipher
        from .crypto.transmissionCipher import TransmissionCipher
        from .crypto.vigenereCipher import VigenereCipher
        from .crypto.indexOfCoincidence import IndexOfCoincidence
        from .crypto.affineCipher import AffineCipher
        from .crypto.oneTimePad import OneTimePad

from pylatex import Document, Section, Subsection, Math,PageStyle, Head, MiniPage, Foot, LargeText, MediumText, simple_page_number, LineBreak
from pylatex.utils import italic, bold
from datetime import date

def generate_latex(caesar : CaesarCipher, transmission : TransmissionCipher, vigenere : VigenereCipher, ioc :IndexOfCoincidence, affine : AffineCipher, otp : OneTimePad) -> None:
    geometry_options = {"margin": "2cm"}
    doc = Document(geometry_options=geometry_options)

    # Add document header
    header = PageStyle("header")

    # Create left header
    with header.create(Head("L")):
        header.append("Page date: ")
        header.append(date.today().strftime("%B %d, %Y"))

    # Create right header
    with header.create(Head("R")):
        header.append("Zafer BALKAN - 212289IVCM")

    # Create right footer
    with header.create(Foot("R")):
        header.append(simple_page_number())

    doc.preamble.append(header)
    doc.change_document_style("header")

     # Add Heading
    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold("1st Assignment")))
        doc.append(LineBreak())
        doc.append(MediumText(bold("ITC8240 CRYPTOGRAPHY - Autumn 2021")))

    # Add body
    with doc.create(Section('Answers')):
        task_1(caesar= caesar, transmission= transmission, doc= doc)
        task_2(vigenere= vigenere, ioc= ioc, doc= doc)
        task_3(affine= affine, doc= doc)
        task_4(otp= otp, doc= doc)
        task_5(doc= doc)

    doc.generate_pdf('docs/1st Assignment', clean_tex=False)

#region Tasks
def task_1(caesar : CaesarCipher, transmission : TransmissionCipher, doc : Document) -> None:
    plain_text = "BLOCKCHAIN"

    temp = caesar.encrypt(plain_text= plain_text, key=9) # S1
    temp = transmission.encrypt(plain_text= temp, key= '51324',padding='x') # P1
    temp = caesar.encrypt(plain_text= temp, key= 19) # S2
    cipher_text = transmission.encrypt(plain_text= temp, key='31425', padding='x') # P2

    with doc.create(Subsection('Task 1')):
        doc.append("Ciphertext: ")
        doc.append(cipher_text)

def task_2(vigenere : VigenereCipher, ioc :IndexOfCoincidence, doc: Document) -> None:
    plain_text = 'FRIENDSMAKETHEWORSTENEMIES'
    key = 'list'

    cipher_text = vigenere.encrypt(plain_text= plain_text, key= key)

    with doc.create(Subsection('Task 2')):
        doc.append("1. Ciphertext: ")
        doc.append(cipher_text)
        doc.append("\n2. IoC of plain text: ")
        doc.append(ioc.calculate(text= plain_text))
        doc.append("\n3. IoC of cipher text: ")
        doc.append(ioc.calculate(text= cipher_text))

def task_3(affine : AffineCipher, doc: Document) -> None:
    plain_text = 'SURFACE'
    cipher_text = 'NJCAXTP'

    with doc.create(Subsection('Task 3')):
        doc.append("1. Encryption key: ")
        doc.append(Math(data=[affine.calculate_encryption_key(plain_text= plain_text, cipher_text= cipher_text)]))
        doc.append("\n2. Decryption key: ")
        doc.append(Math(data=[affine.calculate_decryption_key(plain_text= plain_text, cipher_text= cipher_text)]))
Math(data=['2*3', '=', 9])

def task_4(otp : OneTimePad, doc: Document) -> None:
    key = otp.calculate_key(plain_text= 'DOUGH', cipher_text= '1000000110001010001000100')
    binary_key = otp.encode_binary(plain_text= key)
    cipher_text = otp.encrypt(plain_text= 'GLORY', binary_key= binary_key)

    with doc.create(Subsection('Task 4')):
        doc.append("Ciphertext: ")
        doc.append(cipher_text)

def task_5(doc: Document) -> None:
    with doc.create(Subsection('Bonus Task:')):
        doc.append("//TODO")
#endregion



def main():
    caesar = CaesarCipher()
    transmission  = TransmissionCipher()
    vigenere = VigenereCipher()
    ioc = IndexOfCoincidence()
    affine = AffineCipher()
    otp = OneTimePad()

    generate_latex(caesar= caesar, transmission= transmission, vigenere= vigenere, ioc= ioc, affine= affine, otp= otp)

if __name__ == "__main__":
    main()

