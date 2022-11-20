def remove_parentheses(text):
    result = ""
    inside = False
    spacebar = False

    for l in text:
        if l == "(":
            inside = True
        elif l == ")":
            inside = False
            spacebar = True
        elif not inside:
            if spacebar:
                spacebar = False
            else:
                result += l

    return result

text = "(Nie) jest tak źle"
print(remove_parentheses(text))
