# The alphabet list containing both lowercase and uppercase letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    """
    Encrypts or decrypts a given text using the Caesar cipher.

    Parameters:
    - start_text (str): The input text to be encrypted or decrypted.
    - shift_amount (int): The number of positions to shift the alphabet.
    - cipher_direction (str): Specifies whether to 'encode' or 'decode' the text.

    Returns:
    - None: Prints the result of the encryption or decryption.
    """
    
    end_text = ""
    # Adjust the shift_amount for decoding by multiplying it by -1
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, leave it unchanged
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Main program loop
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Ensure that the shift value is within the range of the alphabet (0 to 25)
    shift = shift % 26

    # Call the caesar function to perform encryption or decryption
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
