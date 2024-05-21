import random
import string

def generador_contraseña(longitud):
    characteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characteres) for i in range(longitud))
    return password

longitud = int(input("Ingrese la longitud de la contraseña: "))
print("Contraseña generada:", generador_contraseña(longitud))
