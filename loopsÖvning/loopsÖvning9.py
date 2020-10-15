name=""
address=""
pin=""
place=""
while (name=="" or address=="" or pin=="" or place==""):
    if name=="" :
        name=input("Mata in ditt namn :")
    if address=="" :
        address= input("Mata in ditt Gatuadress : ")
    if pin=="" :
        pin=input ("Mata in ditt postnummer : ")
    if place=="" :
        place=input ("Mata in ditt postort : ")
print ("Alla uppgifter är ifyllda")