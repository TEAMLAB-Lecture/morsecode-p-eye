# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    user_input = user_input.lower()
    return user_input == "help" or user_input == "h"


def is_validated_english_sentence(user_input):
    if not all([c not in "0123456789_@#$%^&*()-+=[]{}\"\';:\|`~" for c in user_input]):
        return False
    if all([c in ".,!? " for c in user_input]):
        return False
    return True


def is_validated_morse_code(user_input):
    splited = user_input.split()
    if not all([c in "-. " for word in splited for c in word]):
        return False 
    if not all([word in get_morse_code_dict().values() for word in splited]):
        return False
    return True


def get_cleaned_english_sentence(raw_english_sentence):
    return "".join([c for c in raw_english_sentence.strip() if not c in ".,!?"])


def decoding_character(morse_character):
    return next(key for key, val in get_morse_code_dict().items() if val == morse_character)


def encoding_character(english_character):
    return get_morse_code_dict()[english_character.upper()]


def decoding_sentence(morse_sentence):
    temp = []
    for word in morse_sentence.split("  "):
        temp.append("".join([decoding_character(c) for c in word.split()]))
    return " ".join(temp)
 

def encoding_sentence(english_sentence):
    temp = []
    for word in get_cleaned_english_sentence(english_sentence).split():
        temp.append(" ".join([encoding_character(c) for c in word]))
    return "  ".join(temp)


def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while True:
        msg = input("Input your message(H - help, 0 - Exit): ")
        if msg == "0":
            break
        if is_help_command(msg):
            get_help_message()
        elif is_validated_english_sentence(msg):
            encoding_sentence(msg)
        elif is_validated_morse_code(msg):
            decoding_sentence(msg)
        else:
            print("Wrong Input")
    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
