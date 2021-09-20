def __populate_dictionary(cipher_text: str) -> dict:
    char_number_dict = dict()
    length_of_text = len(cipher_text)

    for i in range(0, length_of_text):
        if cipher_text[i] in char_number_dict:
            char_number_dict.update({cipher_text[i] : char_number_dict[cipher_text[i]] + 1})
        else:
            char_number_dict[cipher_text[i]] = 1

    return char_number_dict

def __calculate_sum(dictionary : dict) -> int:
    sum = 0
    for item in dictionary:
        if(dictionary[item] > 1):
            sum = sum + (dictionary[item] * (dictionary[item] -1))
    return sum

def calculate_index_of_coincidence(cipher_text : str) -> float:
    dictionary = __populate_dictionary(cipher_text)
    sum = __calculate_sum(dictionary)
    return sum / (len(cipher_text) * (len(cipher_text) - 1))


print(calculate_index_of_coincidence("EPYEPOPDZSZUFPO"))
