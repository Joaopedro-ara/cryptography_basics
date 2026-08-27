# Decrypt code  for caeser algorithm (brute force)

def decoding_caeser_chifre(cipher_text:str,key:int)->str:
    result=""
    for char in cipher_text.upper():
        if char.isalpha():
            #covert letter to a number(0-25)
            c_number=ord(char)-ord('A')
            # Reverse the shift by subtracting the key
            p_number=(c_number-key)%26
            #Convert back to a letter
            result+=chr(p_number+ ord('A'))
        else:
            # Keep spaces and punctuation as they are
            result += char
    return result

if __name__=="__main__":
    encrypted_text="KHOOR L ORYH VRD EXW WKH EHVW VHULH LV JRPRUDK"
    print(f" Start Attack '{encrypted_text}'")
    # caeser cipper onöy has 25 possible shifts
    for test_key in range(1,26):
        encrypted_text=decoding_caeser_chifre(encrypted_text,test_key)
        # Print every single attempt
        print(f"Trying Key {test_key:02d}: {encrypted_text}")


