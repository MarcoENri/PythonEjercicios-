import random

def adivina_numero():
    number_secret = random.randint(1, 100)
    riddle= None

    while riddle != number_secret:
        riddle = int(input("Adivina el número (entre 1 y 100): "))
        if riddle< number_secret:
            print("Demasiado bajo")
        elif riddle> number_secret:
            print("Demasiado alto")
    
    print("¡Felicitaciones! Adivinaste el número.")

adivina_numero()
