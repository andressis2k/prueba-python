from tabulate import tabulate
from os import system
alumnos = []

def calcular_media(nota1, nota2, nota3):
    return round(((nota1+nota2+nota3)/3),2)

def calcular_calificacion(media):
    if media < 6:
        return "Suspenso"
    if media < 7:
        return "Aprobado"
    if media < 8:
        return "Bien"
    if media < 9:
        return "Notable"
    if media <= 10:
        return "Sobresaliente"
    
def filtrar_aprobados(alumnos):
    aprobados = []
    for alumno in alumnos:
        if alumno["Media"]>= 6:
            aprobados.append(alumno)
    return aprobados

def comprobar_nota(valor):
    try:
        nota = int(valor)
    except:
        print("La nota debe ser un número entero")
        return False
    if nota >=0 and nota <= 10:
        return nota
    else:
        print("Introduzca una nota entre 0 y 10")
        return False

def alta_alumnos():
    nota1, nota2, nota3 = False,False,False
    nombre = input("Introduzca el nombre: ").title()
    apellidos = input("Introduzca los apellidos: ").title()
    while nota1 == False:
        nota1 = comprobar_nota(input("Introduzca la primera nota: "))
    while nota2 == False:
        nota2 = comprobar_nota(input("Introduzca la segunda nota: "))
    while nota3 == False:
        nota3 = comprobar_nota(input("Introduzca la tercera nota: "))
    media = calcular_media(nota1, nota2, nota3)
    calificacion = calcular_calificacion(media)
    return ({"Nombre": nombre, "Apellidos": apellidos, "Nota 1": nota1, "Nota 2": nota2, "Nota 3": nota3, "Media": media, "Calificacion": calificacion})

def borrar_alumno(alumnos):
    limpiar_pantalla()
    cadena = input("Introduzca nombre o apellido: ").lower()
    candidatos = []
    contador = 1
    for indice, alumno in enumerate(alumnos):
        if (cadena in alumno["Nombre"].lower()) or (cadena in alumno["Apellidos"].lower()):
            candidatos.append({"Índice": contador, "Nombre": alumno["Nombre"], "Apellidos": alumno["Apellidos"], "Código alumno": indice})
            contador += 1
    if candidatos:
        valido = False
        while not valido:
            imprimir_lista(candidatos,False)
            entrada = input("Seleccione el usuario a eliminar. Si no es ninguno de ellos, pulse enter: ")
            if entrada == "":
                return alumnos
            try:
                seleccion = int(entrada)
                if seleccion > 0 and seleccion < len(candidatos)+1:
                    valido = True
                else:
                    print("Escoja uno de los alumnos mostrados")
                    input ("Presione enter para continuar")
            except:
                print("Se debe introducir un número")
                input ("Presione enter para continuar")
            
        borrado = alumnos.pop(candidatos[seleccion - 1]["Código alumno"])
        print (f"Se ha borrado el alumno {borrado["Nombre"]} {borrado["Apellidos"]}")
        input ("Presione enter para continuar")      
    else:
        imprimir_lista(candidatos)
    return alumnos

def buscar_alumnos(alumnos):
    buscados=[]
    limpiar_pantalla()
    cadena = input("Introduzca nombre o apellido: ").lower()
    for alumno in alumnos:
        if (cadena in alumno["Nombre"].lower()) or (cadena in alumno["Apellidos"].lower()):
            buscados.append(alumno)
    return buscados

def imprimir_menu():
    limpiar_pantalla()
    print("Bienvenido al sistema de gestión de notas")
    print("1 - Añadir alumno")
    print("2 - Eliminar alumnos")
    print("3 - Mostrar alumnos aprobados")
    print("4 - Buscar alumnos")
    print("5 - Mostrar todos los alumnos")
    print("0 - Salir")

def imprimir_lista(lista,pausa=True):
    limpiar_pantalla()
    if lista:
        print (tabulate(lista, headers="keys"))
    else:
        print ("No se encontraron registros")
    print ("")
    if pausa:
        input ("Presione enter para continuar")      

def limpiar_pantalla():
    system("clear||cls")

while True:
    imprimir_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        alumnos.append (alta_alumnos())
    elif opcion == "2":
        alumnos = borrar_alumno(alumnos)
    elif opcion == "3":
        imprimir_lista(filtrar_aprobados(alumnos))
    elif opcion == "4":
        imprimir_lista(buscar_alumnos(alumnos))
    elif opcion == "5":
        imprimir_lista(alumnos)
    elif opcion == "0":
        print("Hasta luego lucas")
        break
    else:
        print("Por favor, elija una opción válida")
        input ("Presione enter para continuar")

    