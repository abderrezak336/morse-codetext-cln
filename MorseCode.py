from data import morse_code_dict, morse_code_dict_reversed


class MorseCode:

    def __init__(self, text):
        self.new_word = ""
        self.new_phrase = ""
        self.text = text


    def ConvertWordToText(self, word):
        self.new_word = ""
        for w in word.split():
            self.new_word += morse_code_dict_reversed[w]
        return self.new_word

    def ConvertWordToMorseCode(self, word):
        self.new_word = ""
        for s in word:
            self.new_word += morse_code_dict[s]
            self.new_word += " "
        return self.new_word

    def MorseCode(self):
        for item in self.text:
            self.new_phrase += self.ConvertWordToMorseCode(item)
            self.new_phrase += "       "
        return self.new_phrase


    def Text(self):
        for item in self.text:
            self.new_phrase += self.ConvertWordToText(item)
            self.new_phrase += " "
        return self.new_phrase






