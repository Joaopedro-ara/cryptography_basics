import secrets # import the secret modul,which is more secure than the random module
def generate_keystream(lenght:int)->list: # new funcrion to generate the keystream
    keystream=[] # new list where we save the numbers
    #for loop runs (lenght)time ns geneartes a secrets keystream number from 0 to 256
    for i in range(lenght):
        keystream.append(secrets.randbelow(256))
    return keystream # return the complete keystream list back whre the function was called
def xor_cipher(text:str,keystream:list)->str:
    #function take a text string a keystream lis as input and its performs YOR /en/decryption return a result as string
    result="" #iniutialize an empty string to store the final input
    for i in range(len(text)): # lopp trough each charater in the text
        char=text[i]
        key_byte=keystream[i]
        xored_value=ord(char)^key_byte #convert character to number (ord), then XOR it with the key byte
        result+=chr(xored_value) # convert the Xor rresult back to a character and add it to the result string
    return result

if __name__=="__main__":
    message="WTF happen to the Petrol price " #original message
    msg_lenght=len(message) # Measure the lenght of the text
    my_kystream=generate_keystream(msg_lenght) #generate a keystream of the same lenght
    #ds=generate_keystream(msg_lenght)
    print("Keystream: ",my_kystream)
    cipher_text=xor_cipher(message,my_kystream) #encrypt the message
    print("Encrypt:",cipher_text)
    decrypte_text=xor_cipher(cipher_text,my_kystream) # decrpyt text
    print("Decrypt:",decrypte_text)
