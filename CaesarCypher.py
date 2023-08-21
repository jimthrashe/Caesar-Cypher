import random
import uuid
import os

def caesar_cipher(plaintext, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted_text = ""

    for char in plaintext:
        if char.isalpha():
            char_case = char.upper()
            char_index = alphabet.index(char_case)
            shifted_index = (char_index + shift) % 26
            encrypted_char = alphabet[shifted_index]
            if char.islower():
                encrypted_char = encrypted_char.lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    file_path = input("Enter the path of the .txt file to read: ")
    
    try:
        with open(file_path, 'r') as file:
            plaintext = file.read().strip()  # Read the content of the file and remove leading/trailing whitespace
    except FileNotFoundError:
        print("File not found.")
        return
    
    random_shift = random.randint(1, 25)  # Generate a random shift value between 1 and 25
    encrypted_text = caesar_cipher(plaintext, random_shift)
    
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Generate a unique file name using uuid
    output_file_name = f"Encrypted_{uuid.uuid4().hex}.txt"
    
    output_file_path = os.path.join(script_dir, output_file_name)
    
    with open(output_file_path, 'w') as file:
        file.write(encrypted_text)
        
    print(f"Text from file encrypted with random shift {random_shift} and written to '{output_file_path}'.")

if __name__ == "__main__":
    main()

