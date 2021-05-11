from caesar_art import logo

print(logo)

alphabet =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}")

    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")


# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         if new_position > 26:
#             new_position = new_position % 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     uncoded_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         if new_position < 0:
#             new_position = new_position + 26
#         new_letter = alphabet[new_position]
#         uncoded_text += new_letter
#     print(f"The encoded text is {uncoded_text}")
        

# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)