def berakna_kontrollsiffra(personnummer):
    personnummer = [int(x) for x in str(personnummer)]

    # Multiplicera varannan siffra från höger med 2
    for i in range(0, len(personnummer), 2):
        personnummer[i] *= 2
        if personnummer[i] > 9:
            personnummer[i] -= 9

    # Beräkna summan av alla siffror
    summa = sum(personnummer)

    # Beräkna kontrollsiffran
    kontrollsiffra = (10 - (summa % 10)) % 10

    return kontrollsiffra

def verifiera_personnummer(personnummer):
    inmatad_kontrollsiffra=int(personnummer[-1])
    personnummer_utan_kontrollsiffra=personnummer[:-1]
    

# Ta in personnummer utan kontrollsiffra som input
input_personnummer = input("Ange ditt personnummer (10 siffror utan kontrollsiffra): ")

# Beräkna kontrollsiffran
kontrollsiffra = berakna_kontrollsiffra(input_personnummer)

print(f"Den beräknade kontrollsiffran är: {kontrollsiffra}")