from re import M
from textwrap import fill
import numpy as np

peliculas = [{"nombre": "Super marios bros 2D"}]
asientos_ocupados = 33
valor_entrada = 2500
nombres = []
contador = 0


def lista_pelicula():
    for i in range(len(peliculas)):
        print(f"[{i+1}] {peliculas[i]}]")

def lista_asientos():
    lista = np.zeros((10,15))
    return lista

def buscar_asientos(asientos,fila,columna):
    if asientos[fila,columna] == asientos_ocupados:
        return True
    
    return False 

def solicitar_asientos(asientos):
    contador = 1

    while True:
        while True:

            fila = int(input("Fila asientos 1-10:"))-1
            columna = int(input("Columna asientos 1-15:"))-1

            if (buscar_asientos(asientos,fila,columna)):
                print("Ya existe")
            else:
                break
    
        asientos[fila,columna] = asientos_ocupados
        contador += 1

        if (contador > 1):
            break
    nombre = input("Cual es su nombre?:")
    nombres.append({"Nombre": nombre, "Fila": fila, "Columna": columna})

def menu():
    print(f"Pelicula en cartelera: {peliculas}")
    lista_menu=["Butacas disponibles", "Comprar entrada", "Ver boleta"]
    
    for i in range(len(lista_menu)):
        print(f"[{i+1}] {lista_menu[i]}")

    while True:
        try:
            opc = int(input("Elija la opcion deseada: "))
            if opc > 0 or opc < 3:
                break
            else:
                print("Error, vuelva a intentarlo.")
        except ValueError:
            print("Error, vuelva a intentarlo.")

    if opc == 1:
        print(asientos)
    elif opc == 2:
        comprar_entrada()
    elif opc == 3:
        boleta_menu()

def boucher(mensaje):
    archivo = open("Boleta.txt","w")
    archivo.write(str(mensaje)+"\n")
    archivo.close()

def comprar_entrada():
    while True:
        try:
            duoc = int(input("Es alumno duoc? (1SI, 2NO)"))
            if duoc > 0 or duoc < 3:
                break
            else:
                print("Error, vuelva a intentarlo.")
        except ValueError:
            print("Error, vuelva a intentarlo.")
    
    if duoc == 1:
        print("Tienes un 60% de descuento por ser alumnos duoc")
        desc_entrada = valor_entrada * 0.6
        desc_entrada = round(desc_entrada)
        print(f"Precio pelicula: ${desc_entrada}")
        
    elif duoc == 2:
        print(f"Precio pelicula: ${valor_entrada}")

    solicitar_asientos(asientos)
    print(asientos)

    global contador
    contador += 1

    if duoc == 1:
        boleta =f"""
         ************************
         ***    CINEDUOC  #{contador}  ***
         ************************ 
         {nombres}
         Alumno Duoc

         Descuento 60%
         Precio:{desc_entrada}
         ************************
         ******* CINEDUOC *******
         ************************"""
    elif duoc == 2:
        boleta =f"""    
         ************************
         ***    CINEDUOC  #{contador}  ***
         ************************ 
         {nombres}
         Precio: {valor_entrada}
         ************************
         ******* CINEDUOC *******
         ************************"""
    
    boucher(boleta)

def boleta_menu():
    try:
        b = open("boleta.txt", "r")
        imp_boleta = b.read()
        print(imp_boleta)
    except FileNotFoundError:
        print("No se puede encontrar el archivo")

asientos = lista_asientos()
menu()
while True:
    print("Desea seguir? (1SI, 2NO)")
    while True:
        try:
            opc = int(input("Ingrese la opcion deseada: "))
            if opc > 0 or opc < 3:
                break
            else:
                print("Error, vuelva a intentarlo.")
        except ValueError:
            print("Error, vuelva a intentarlo.")
    if opc == 1:
        menu()
    elif opc == 2:
        break
