alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


# Caesar Encrip
def caesar_encrip(x):
    newalphabet = ""
    thing = ""
    for i in alphabet:
        newalphabet += alphabet[(alphabet.index(i) + key) % len(alphabet)]

    # print(newalphabet)
    for letter in user_text:
        if letter in alphabet:
            thing += newalphabet[alphabet.index(letter)]
        else:
            thing += letter
    print(thing)


# Caesar Decrip
def caesar_decrip(x):
    newalphabet = ""
    thing = ""
    for i in alphabet:
        newalphabet += alphabet[(alphabet.index(i) - key) % len(alphabet)]

    # print(newalphabet)

    for letter in user_text:
        if letter in alphabet:
            thing += newalphabet[alphabet.index(letter)]
        else:
            thing += letter
    print(thing)


print("Which Cipher Do You Want to Use?")

# USER INTERFACE
chosen_one = int(input("1 - Caesar_Encrip  2 - Caesar_Decrip"))
user_text = input("Enter your text ")
print(user_text)
key = int(input("Enter the key, it must be an integer "))

# asking to choose
if chosen_one == 1:
    # print("lol")
    caesar_encrip(user_text)
elif chosen_one == 2:
    # print("dada")
    caesar_decrip(user_text)
else:
    print("Your number doesn't match, Restart the program")
