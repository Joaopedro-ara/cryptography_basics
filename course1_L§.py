# Function to perform XOR between the text and the key
def apply_xor(text, key):
    result = ""

    # Loop through both text and key simultaneously using zip()
    for t_char, k_char in zip(text, key):
        # ord() converts char to integer, ^ performs XOR, chr() converts back to char
        xored_char = chr(ord(t_char) ^ ord(k_char))

        # Append to the result string
        result += xored_char

    return result


# Main execution block
if __name__ == "__main__":
    plaintext = "HELLO"
    key = "XMCKL"  # Key must be exactly the same length!

    # 1. Encryption
    ciphertext = apply_xor(plaintext, key)
    print(f"Encrypted: {repr(ciphertext)}")  # Using repr() to show non-printable characters

    # 2. Decryption
    decrypted = apply_xor(ciphertext, key)
    print(f"Decrypted: {decrypted}")