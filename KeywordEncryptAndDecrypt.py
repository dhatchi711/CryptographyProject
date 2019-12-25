alphabet =["a", "b", "c", "d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def keyword_encrip(x):
    keyword = input("Enter a keyword: ")
    newalphabet = []
    print(newalphabet)
    for letter in keyword:
        if letter not in newalphabet:
            newalphabet += letter
    print(newalphabet)
    for letter in alphabet:
        if letter not in newalphabet:
            newalphabet += letter
    print(newalphabet)
    thing = ""
    for letter in x:
        if letter in alphabet:
            # print (newalphabet)
            thing += newalphabet[alphabet.index(letter)]
        else:
            thing += letter
    print(thing)


# Keyboard Decrip
def keyword_decrip(x):
    keyword = input("Enter a keyword: ")
    newalphabet = []

    for letter in keyword:
        if letter not in newalphabet:
            newalphabet += letter

    for letter in alphabet:
        if letter not in newalphabet:
            newalphabet += letter

    thing = ""
    for letter in x:
        if letter in alphabet:
            thing += alphabet[newalphabet.index(letter)]
            # print(alphabet)
        else:
            thing += letter
    print(thing)
