# this code is an Auto _coding from the decoding_caeser_chifre
# This algorithm cracks the Caesar cipher by automatically assuming
# the most frequent letter in the ciphertext is the letter 'E'.
def decrypt_text(cipher_text:str, key:int)-> str:
    result=""
    for char in cipher_text.upper():
        if char.isalpha():
            c_number = ord(char) - ord('A')
            p_number = (c_number - key) % 26
            result += chr(p_number + ord('A'))
        else:
            result += char
    return result

def smart_crack(cipher_text:str)-> tuple:
    pass
