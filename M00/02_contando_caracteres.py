"""
# Inicial
while True:
    cadena = input("Introduzca una cadena:")
    print (f"La cadena '{cadena}' tiene {len(cadena)} caracteres")
"""

"""
# Retos
while True:
    cadena = input("Introduzca una cadena:")
    if cadena == "":
        print ("Escribe algo, no seas tímido")
        continue
    print (f"La cadena '{cadena}' tiene {len(cadena)} caracteres")
"""
# Sin usar función len
while True:
    longitud = 0
    cadena = input("Introduzca una cadena:")
    if cadena == "":
        print ("Escribe algo, no seas tímido")
        continue
    for char in cadena:
        longitud += 1
    print (f"La cadena '{cadena}' tiene {longitud} caracteres")
