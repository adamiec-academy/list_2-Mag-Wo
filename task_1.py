def remove_parentheses(text):
    result = ""
    inside = False

    for l in text:
        if l == "(":
            inside == True
        elif l == ")":
            inside == True
        elif str.index(text,"(") < str.index(text,l) < str.index(text,")"):
            inside == True
        elif inside == True:
            pass
        else:
            result += l


    return result

 text = "(Nie) jest tak źle"

print(remove_parentheses(text))

