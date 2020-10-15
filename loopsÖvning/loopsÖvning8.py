try:
    a=int(input("Mata in ett tal : "))
    if a<30 :
        for x in range (a,31) :
            print(x)
    else :
        print ("Du har matat in ett felaktigt tal")
except :
    print ("Du har matat in ett ogiltigt tal")
