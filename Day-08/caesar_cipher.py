import art


to_continue = True
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text,shift,direction):

    string=""
    for letter in text:
        if letter in alphabet:
            pos_of_letter = alphabet.index(letter)
            if direction == "encode":
                required_pos = (pos_of_letter + shift) % 25
                string += alphabet[required_pos]
            else:
                required_pos = (pos_of_letter - shift) % 25
                string += alphabet[required_pos]
        else:
            string += letter
    print(f"{direction}d text: {string}")


def user_input():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)


while to_continue == True:
    if ask == "yes":
        user_input()
    else:
        to_continue = False
    ask = input("Do you want to continue, yes or no: ").lower()

'''
def encrypt(text,shift):

    encrypted_list=[]
    encrypted_text=""
    words = text.split(" ")
    for word in words:
        string=""
        for letter in word:
            pos_of_letter = alphabet.index(letter)
            required_position = pos_of_letter + shift
            string += alphabet[required_position]
        encrypted_list.append(string)
    encrypted_text = ''.join(encrypted_list)

    print(f"Encrypted text: {encrypted_text}")


def decrypt(cipher,shift):

    plain_text=""
    cipher_list = cipher.split(" ")
    plain=[]
    for word in cipher_list:
        string=""
        for letter in word:
            pos_of_letter = alphabet.index(letter)
            required_position = pos_of_letter - shift
            string += alphabet[required_position]
        plain.append(string)
    plain_text = " ".join(plain)

    print(f"Decrypted text: {plain_text}")

'''