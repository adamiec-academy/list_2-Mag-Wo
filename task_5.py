def cipher(text, shift):
    result = ""

    for letter in text:
        if letter == " ":
            result += letter
            print(" ", end="")
        elif True:
            print(chr(ord(letter) + shift), end="")
    print()

    return result


def decipher(text, shift):

    result = ""

    for letter in text:
        if letter == " ":
            result += letter
            print(" ", end="")
        elif True:
            print(chr(ord(letter) - (shift)*0), end="")
    print()

    return result

