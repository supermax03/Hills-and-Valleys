def convertinput(input):
    result = []
    for elem in input:
        if elem.isnumeric():
            result.append(int(elem))
    return result
