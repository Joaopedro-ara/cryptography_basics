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
    #dict for the letters
    frequencies={}
    for char in cipher_text.upper():
        if char.isalpha(): #if sign is a character then go on
            frequencies[char]=frequencies.get(char,0)+1 #if is a chracter we increment de dict ,if not we startet again at 0

    #>lets find the charcter with the highst increment
    most_comon_char=max(frequencies,key=frequencies.get)
    #distance to E because E is the most character frequencie
    distance=ord(most_comon_char)-ord("E")
    calculated_key=distance %26
    hacked_massage=decrypt_text(cipher_text,calculated_key) # we want to decryt the message
    return calculated_key,hacked_massage,most_comon_char

if __name__=="__main__":
    encrypted_message="KHOOR L ORYH VRD EXW WKH EHVW VHULH LV JRPRUDK"
    print("Initiating Automatic Frequency Analysis...\n")
    key,cracked_text,top_letter=smart_crack(encrypted_message) # we call the smart_crackte_funktion
    print(">>> CRACKING COMPLETE <<<")
    print(f"Most frequent letter found: '{top_letter}'")
    print(f"Calculated Key: {key}")
    print(f"Decrypted Message:\n{cracked_text}")