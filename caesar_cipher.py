
def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts text using Caesar Cipher.

    Args:
    - text (str): Input text.
    - shift (int): Shift value.
    - direction (str): 'encrypt' or 'decrypt'.

    Returns:
    - result (str): Encrypted or decrypted text.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.lower())
            if direction == 'encrypt':
                new_index = (index + shift) % 26
            elif direction == 'decrypt':
                new_index = (index - shift) % 26
            if char.isupper():
                result += alphabet[new_index].upper()
            else:
                result += alphabet[new_index]
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")

    while True:
        print("Options:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted text: {decrypted_text}")
        elif choice == '3':
            print("Goodbye!")
            break
        else: 
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
