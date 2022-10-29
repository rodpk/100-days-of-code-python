import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

## my solution
def caesar(input_text, shift_amount, direction):
    input_text = input_text.lower()
    new_text = ''

    if (direction == 'encrypt'):
        for letter in input_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount

            if (new_position > 25):
                to_shift = new_position - 26
                new_position = to_shift
            new_text += alphabet[new_position]

    elif (direction == 'decrypt'):
        for letter in input_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount

            if (new_position < 0):
                to_shift = 26 - new_position
                new_position = to_shift
            new_text += alphabet[new_position]
    
    return new_text
## course solution
def caesar_2(start_text, shift_amount, cipher_direction):
    start_text = start_text.lower()
    end_text = ''

    if cipher_direction == "decode":
        shift_amount *= -1
    
    for char in start_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if (new_position > 25):
                to_shift = new_position - 26
                new_position = to_shift
            
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction} of {start_text} text is {end_text}')

running = True

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift =  shift % 26

    caesar_2(text, shift, direction)

    aswr = input('Do you want to try again? (y/n): ').lower()

    if (aswr == 'n'):
        running = False


print('Goodbye!')