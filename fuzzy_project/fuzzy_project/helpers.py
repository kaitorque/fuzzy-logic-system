def checkEmpty(input):
    error = []
    for x in input:
        if x.value ==  "":
            error.append(x.name+" cannot be empty.")
    return error

def checkDigit(input):
    error = []
    for x in input:
        try:
            int(x.value)
        except ValueError:
            error.append(x.name+" is not an integer.")
    return error
