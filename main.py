# main.py

from sumar import sumar
from restar import restar
from mutiplicacion import multiplicar
from dividir import dividir
from SumaAvanzada import SumaAvanzada

def mostrar_menu():
    print("Calculator")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        a = float(input("Escribe el primer número: "))
        b = float(input("Escribe el segundo número: "))
        print(f"Resultado: {sumar(a, b)}")
    elif opcion == 2:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"Resultado: {restar(a, b)}")
    elif opcion == 3:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"Resultado: {multiplicar(a, b)}")
    elif opcion == 4:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(f"Resultado: {dividir(a, b)}")
    elif opcion == 5:
        numeros = list(map(float, input("Introduce los números separados por espacio: ").split()))
        print(f"Resultado: {SumaAvanzada(numeros)}")
    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opción inválida")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Elige una opción: "))
        if opcion == 6:
            break
        ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()
