def remove_parentheses(text):
    result = ""
    inside = False

    for l in text:
        if l == "(":
            inside = True
        elif l == ")":
            inside = False
        elif not inside:
            result += l

    return result

text = "(Nie) jest tak źle"
print(remove_parentheses(text))
