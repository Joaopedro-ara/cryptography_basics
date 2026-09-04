#This projekt is About to read a word file and decrypt the file.
# im port docx
from docx import Document

#encoding text with  caeser cifre
def encrypt_text(text:str,key:int)->str:
    result="" #start with empty  text
    for char in text.upper():
        if char.isalpha():
            p_number=ord(char)-ord('A')
            c_number=(p_number +key) %26
            result+=chr(c_number+ ord('A'))
        else:
            result+=char
    return result


if __name__=="__main__":
    doc =Document("caeser-chifre.docx") #
    full_text=" "
    # Loop through all paragraphs and combine their text into one string
    for para in doc.paragraphs:
        full_text+=para.text+ " "
    cipher_text=encrypt_text(full_text,5) #Here we call the encrypt_text function and pass it the full_text variable and the key.
    # Here we create a new document, add the encrypted text to it,
    # and save it as a new Word document.
    new_doc=Document()
    new_doc.add_paragraph(cipher_text)
    new_doc.save("Encryptet_caeser.docx")
    print("Word-File successfully encrypted and saved!")

