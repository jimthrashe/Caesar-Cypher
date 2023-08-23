def caesar_decrypt(ciphertext):
    decrypted_results = []

    for shift in range(1, 25):
        decrypted_text = ""

        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')

                decrypted_char = chr((ord(char) - base - shift+25) % 25 + base)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        decrypted_results.append(decrypted_text)

    return decrypted_results

# Read ciphertext from a .txt file
def read_ciphertext_from_file(filename):
    with open(filename, 'r') as file:
        ciphertext = file.read()
    return ciphertext

# Example usage
file_path = input(".txt file")
ciphertext = read_ciphertext_from_file(file_path)
decrypted_messages = caesar_decrypt(ciphertext)

for i, message in enumerate(decrypted_messages):
    print(f"Shift {i+1}: {message}")
