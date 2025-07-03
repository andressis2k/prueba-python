def comprobarnum(entrada):
    for char in entrada:
        if char not in "0123456789":
            return False
    return True

while True:

    entrada1 = input("Introduzca el primer número: ")
    if entrada1.isnumeric():
        n1 = int(entrada1)
    else:
        print("El primer número no es un entero")
        continue

    entrada2 = input("Introduzca el segundo número: ")
    if entrada2.isnumeric():
        n2 = int(entrada2)
    else:
        print("El segundo número no es un entero")
        continue

    salida = f"La suma de {n1} + {n2} es {n1+n2}\nEl producto de {n1} x {n2} es {n1*n2}\nLa resta de {n1} - {n2} es {n1-n2}\nLa división de {n1} / {n2} es {n1/n2}"

    print(salida)