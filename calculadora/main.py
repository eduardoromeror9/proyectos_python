def suma(a, b):
    result = a + b
    print(f'La suma de {a} + {b} = {result}')


def resta(a, b):
    result = a - b
    print(f'La resta de {a} - {b} = {result}')


def multiplicacion(a, b):
    result = a * b
    print(f'La multiplicacion de {a} * {b} = {result}')


def division(a, b):
    result = a / b
    print(f'La division de {a} / {b} = {result}')


calculadora = """
A. Suma
B. Resta
C. Multiplicacion
D. Division
E. Salir
"""
while True:
    print(calculadora)
    opcion = input('Ingrese una opcion: ')
    
    if opcion == 'A' or opcion == 'a':
        print('### Suma ###')
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        suma(a, b)
    elif opcion == 'B' or opcion == 'b':
        print('### Resta ###')
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        resta(a, b)
    elif opcion == 'C' or opcion == 'c':
        print('### Multiplicacion ###')
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        multiplicacion(a, b)
    elif opcion == 'D' or opcion == 'd':
        print('### Division ###')
        a = int(input('Ingrese el primer numero: '))
        b = int(input('Ingrese el segundo numero: '))
        division(a, b)
    elif opcion == 'E' or opcion == 'e':
        print('### Salir ###')
        print('Gracias por usar la calculadora')
        quit()
    else:
        print('Opcion incorrecta')

###! Otra opcion de calculadora ###

# def calculadora():

#     while True:
#         print('Calculadora de operaciones básicas')
#         print("1. Suma")
#         print("2. Resta")
#         print("3. Multiplicación")
#         print("4. División")
#         print("5. Salir")

#         operacion = int(input("Ingrese la operación a realizar: "))

#         if operacion == 5:
#             print("Hasta luego")
#             quit()
#         elif operacion < 1 or operacion > 5:
#             print("\n Operación no válida \n")
#             continue

#         num1 = int(input("Por favor, ingrese el primer número: "))
#         num2 = int(input("Por favor, ingrese el segundo número: "))

#         if operacion == 1:
#             print(f'La suma de {num1} + {num2} = {num1 + num2}')
#         elif operacion == 2:
#             print(f'La resta de {num1} - {num2} = {num1 - num2}')
#         elif operacion == 3:
#             print(f'La multiplicación de {num1} * {num2} = {num1 * num2}')
#         elif operacion == 4:
#             print(f'La división de {num1} / {num2} = {num1 / num2}')

# calculadora()