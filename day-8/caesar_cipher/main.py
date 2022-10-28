alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encrypted_word = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount

        if (new_position > 25):
            to_shift = new_position - 26
            new_position = to_shift
        encrypted_word += alphabet[new_position]
    return encrypted_word


cript = encrypt('zy', 1)
print(cript)

