#This projekt is About to read a word file and decrypt the file.
# im port docx
from docx import Document
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
    hacked_massage=decrypt_text(cipher_text,calculated_key)  #The decrypted message is stored in the new variable using the calculated key.
    return calculated_key,hacked_massage,most_comon_char

if __name__=="__main__":
    doc=Document("Encryptet_caeser.docx")
    encrypte_text = ""
    for para in doc.paragraphs:
        encrypte_text+=para.text+" "
    key,hacked_text,top_letter=smart_crack(encrypte_text)
    cracked_doc=Document()
    cracked_doc.add_paragraph(hacked_text)
    cracked_doc.add_paragraph(f"Crack wit the key: {key}")
    cracked_doc.save("Cracked_chiffre_caeser.docx")
    print("The word Word-file is decrypt now ")


