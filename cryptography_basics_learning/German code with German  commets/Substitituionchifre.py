# Substitutionschiffre -> Hier kann jeder Buchstabe des Alphabets durch ein x beliebigen  anderen Buchstaben erstez werden
#-> Beispiel aus wid X ,b-> M .. Dadurch ergibt sich 26! (4.10^26) mögliche >Schlüssel

def verschluessen(text,schluessel):
    # Standart Alphabet als Referenz
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #wandeln den Eingabetext un Großbuchstaben um , um einfacher zu machen
    text=text.upper()
    geheimtext=""
    # for schleifen um durch jeden Buchstabe zu gehen
    for zeichen in text:
        # mit if else prüfen wir ob das zeichen ein Normaler Buchstabe ist
        if zeichen in alphabet:
            #finde die Position(index) des Buchstabens im normalen alphabet
            index=alphabet.find(zeichen)
            #nimm den Buchstaben an derselben Position aus dem Schlüssel
            geheimtext+=schluessel[index]
        else:
            #Leerzeichen,zahlen und satzzeichen bleinen unverändert
            geheimtext+=zeichen
    return geheimtext

def entschluesseln(geheimtext,schluessel):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    klartext=""
    for zeichen in geheimtext:
        if zeichen in schluessel:
            #Umgekehrt: suchen die Position im schlüssel
            index=schluessel.index(zeichen)
            # und nehmen den Buchstaben an dieser Stelle aus dem normalen Alphabet
            klartext+=alphabet[index]
        else:
            klartext+=zeichen
    return klartext
# testlauf
mein_schluessel = "QWERTZUIOPASDFGHJKLYXCVBNM"
nachricht="Heute greife ich Rom an"
verschluesselt=verschluessen(nachricht,mein_schluessel)
entschluesselt=entschluesseln(verschluesselt,mein_schluessel)
print("Original:      ", nachricht)
print("Verschlüsselt: ", verschluesselt)
print("Entschlüsselt: ", entschluesselt)