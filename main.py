from MorseCode import MorseCode


if __name__== '__main__':
    ask_user = str(input("Write 'M' to encode in morse code and 'D' to decode or 'Q' to quit: ").upper())

    while(ask_user != "Q"):
        user_text = str(input("Write your text please: ").upper())
        if (ask_user == "M"):
            morse_code = MorseCode(user_text.split())
            print(morse_code.MorseCode())

        elif (ask_user == "D"):
            morse_code = MorseCode(user_text.split("       "))
            print(morse_code.Text())

        else:
            print("Invalid input!")

        ask_user = str(input("Write 'M' to encode in morse code and 'D' to decode or 'Q' to quit: ").upper())

