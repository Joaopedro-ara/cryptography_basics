import os
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms
def encrypt_chacha20(message:str):
    message_bytes=message.encode('utf-8') # CHACHA_20 is a modern Algorithm so the acept only bytes
    key=os.urandom(32) # 32 bytes to genereate a key of 256 bytes
    nonce=os.urandom(16) #16 bytes for the nonce
    algorithm=algorithms.ChaCha20(key,nonce) # call the chacha
    cipher=Cipher(algorithm,mode=None)
    encrypthor=cipher.encryptor()
    ciphertext=encrypthor.update(message_bytes)
    return ciphertext,key,nonce
def decrypt_chacha20(ciphertext,key,nonce):
    algorithm=algorithms.ChaCha20(key,nonce)
    cipher=Cipher(algorithm,mode=None)
    decrypthor=cipher.decryptor()
    ciphertext=decrypthor.update(ciphertext)
    return ciphertext.decode("utf-8")

if __name__=="__main__":
    message="Send this message to our Agent:Code007, you are cleared to execute the mission. You are free to go!"
    ct,k,n=encrypt_chacha20(message)
    print("chipertext: ",ct)
    print("Key:",k)
    print("Nonce:",n)
    pt=decrypt_chacha20(ct,k,n)
    print("Decrypted:",pt)
