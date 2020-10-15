while True :
    print ("Rolling the dices...")
    print("The values are...")
    import random
    for x in range(2):
        print (random.randint(1,6))
    val=input("Roll the dices again? y/n: ")
    if val!="y":
        break

