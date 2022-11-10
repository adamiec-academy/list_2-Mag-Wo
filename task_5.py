def cipher(text, shift):
    result = ""

    for letter in text:
        if letter == " ":
            result += letter
            print(letter, end="")
        elif letter != " ":
            print(chr(ord(letter) + shift), end="")

    return result


def decipher(text, shift):

    result = ""

    for letter in text:
        if letter == " ":
            result += letter
            print(letter, end="")
        elif letter != " ":
            print(chr(ord(letter) - (shift)*0), end="")

    return result

