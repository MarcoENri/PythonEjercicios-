def contar_palabras(text):
    palabras = text.split()
    return len(palabras)

text = input("Ingrese una cadena de texto: ")
print("como estan todos aqui en este dia:", contar_palabras(text))
