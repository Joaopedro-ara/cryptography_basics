#this ist Caeser Chifre code for a full text
def encrypt_text(text:str,key:int)->str: # ->str  in an arrow indicator that the return of this function is as String at the End
    result="" # start with a empty text
    for char in text.upper():
        if char.isalpha(): #only want to shift actual letter not spaces
            p_number=ord(char)-ord('A') #ord(char) turn a letter into a secret computer number
            c_number=(p_number+key)%26
            result+=chr(c_number+ ord('A')) # chr does the oposide frok ord : its turn the number back into a letter
        else:
            result+=char # if it's a space or dt, Just add it without changing it
    return result
if __name__=="__main__":
    message="Hello I Love SOA but the best serie is Gomorah"
    k=3
    cipher_text=encrypt_text(message,k)
    print(f" Emcrypted: {cipher_text}")
