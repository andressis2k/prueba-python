import random
"""
entrada = input("Introduced un nombre: ")
salida = f"Hola {entrada}, ¿qué tal?"

print (salida)
"""

"""
# Sin usar variables
while True:
    print (f"Hola {input("Introduced un nombre: ")}, ¿qué tal?")
"""

saludos = [
    "¿qué tal?", 
    "que tengas un buen día",
    "¡cuánto tiempo sin verte!", 
    "da recuerdos a la familia",
    "choca esos cinco"
    ]

while True:
    nombre = input("Introduced un nombre: ")
    i = random.randint(0,len(saludos)-1)
    print (f"Hola {nombre}, {saludos[i]}")