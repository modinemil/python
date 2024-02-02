text = input()

text = text.upper()

vokaler = ("A", "O", "U", "Å", "E", "I", "Y", "Ä", "Ö")

output = ""

for bokstav in text:
    bokstav = bokstav.upper()
    
    if bokstav == "A" or bokstav == "O" or bokstav == "U" or bokstav == "Å" or bokstav == "E" or bokstav == "I" or bokstav == "Y" or bokstav == "Ä" or bokstav == "Ö":
        output += "E"
    else:
        output += bokstav

print(output)