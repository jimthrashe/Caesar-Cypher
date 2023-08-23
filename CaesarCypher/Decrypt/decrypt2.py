def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def caesar_brute_force(ciphertext):
    decrypted_results = []

    for shift in range(26):
        decrypted_message = caesar_decrypt(ciphertext, shift)
        decrypted_results.append(decrypted_message)

    return decrypted_results

def main():
    file_path = input("Enter the path of the encrypted .txt file to decrypt: ")
    
    try:
        with open(file_path, 'r') as file:
            encrypted_text = file.read().strip()  # Read the content of the file and remove leading/trailing whitespace
    except FileNotFoundError:
        print("File not found.")
        return
    
    decrypted_messages = caesar_brute_force(encrypted_text)
    
    print("Possible Decrypted Messages:")
    for i, message in enumerate(decrypted_messages):
        print(f"Shift {i+1}: {message}")

if __name__ == "__main__":
    main()

