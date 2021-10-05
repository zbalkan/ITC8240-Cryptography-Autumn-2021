class IndexOfCoincidence:

    def __init__(self):
        print("An instance of class IndexOfCoincidence is initiated.")

    def __str__(self):
        return "Calculate Index of Coincidence."
    #region Public Methods
    def calculate_index_of_coincidence(self, cipher_text : str) -> float:
        dictionary = self.__populate_dictionary(cipher_text)
        sum_of_chars = self.__calculate_sum(dictionary)
        return sum_of_chars / (len(cipher_text) * (len(cipher_text) - 1))
    #endregion

    #region Private Methods
    def __populate_dictionary(self, cipher_text: str) -> dict:
        char_number_dict = dict()
        length_of_text = len(cipher_text)

        for i in range(0, length_of_text):
            if cipher_text[i] in char_number_dict:
                char_number_dict.update({cipher_text[i] : char_number_dict[cipher_text[i]] + 1})
            else:
                char_number_dict[cipher_text[i]] = 1

        return char_number_dict

    def __calculate_sum(self, dictionary : dict) -> int:
        sum_of_chars = 0
        for item in dictionary:
            if(dictionary[item] > 1):
                sum_of_chars = sum_of_chars + (dictionary[item] * (dictionary[item] -1))
        return sum_of_chars
    #endregion
